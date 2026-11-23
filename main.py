import os

out_dir = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
    f.write(b"yuniasandria")
