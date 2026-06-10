from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

BASE = Path('/home/user/gomi-app')
ICON_DIR = BASE / 'icons'
ICON_DIR.mkdir(parents=True, exist_ok=True)

BG = '#2f855a'
PANEL = '#ffffff'
TEXT = '#1f2937'
WHITE = '#ffffff'
BURN = '#4caf50'
NONBURN = '#f4d03f'
RESOURCE = '#5dade2'
PLASTIC = '#c97b30'
HAZARD = '#d96ca6'

sizes = [192, 512]

for size in sizes:
    img = Image.new('RGBA', (size, size), BG)
    draw = ImageDraw.Draw(img)

    margin = int(size * 0.1)
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=int(size * 0.08),
        fill=PANEL
    )

    dot_size = int(size * 0.12)
    gap = int(size * 0.04)
    start_x = int(size * 0.2)
    y = int(size * 0.22)
    colors = [BURN, NONBURN, RESOURCE, PLASTIC, HAZARD]
    for i, color in enumerate(colors):
        x = start_x + i * (dot_size + gap)
        draw.ellipse([x, y, x + dot_size, y + dot_size], fill=color)

    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc', int(size * 0.16))
        font_small = ImageFont.truetype('/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc', int(size * 0.1))
    except Exception:
        font = ImageFont.load_default()
        font_small = ImageFont.load_default()

    title = 'ごみ'
    subtitle = '今日'

    bbox = draw.textbbox((0, 0), title, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text(((size - w) / 2, size * 0.45), title, font=font, fill=TEXT)

    bbox2 = draw.textbbox((0, 0), subtitle, font=font_small)
    w2 = bbox2[2] - bbox2[0]
    draw.text(((size - w2) / 2, size * 0.68), subtitle, font=font_small, fill=BG)

    img.save(ICON_DIR / f'icon-{size}.png')

print('icons created')