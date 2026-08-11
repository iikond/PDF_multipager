from pathlib import Path

from PIL import Image

output_dir = Path("pdf")
output_dir.mkdir(exist_ok=True)

files = {}

for file in Path(".").glob("*.bmp"):
    doc, page = map(int, file.stem.split("_"))
    files.setdefault(doc, []).append((page, file))

for doc, pages in files.items():
    pages.sort()

    images = []

    for _, path in pages:
        img = Image.open(path).convert("RGB")
        images.append(img)
    
    images[0].save(
        output_dir / f"{doc}.pdf",
        save_all=True,
        append_images=images[1:]
    )
    
print("Готово.")
#i love linux.
