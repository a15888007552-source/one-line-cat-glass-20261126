"""Write the cat's excuse to /output/entry.txt.

Reads the output directory from MAKEFUN_OUTPUT_DIR when set, else /output.
"""

from pathlib import Path
import os

LINE = "That glass had been leaning toward the edge all week, and I simply gave gravity the nudge it was already asking for — call it assisted relocation, not a crime."

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
