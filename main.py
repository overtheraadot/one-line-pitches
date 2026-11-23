"""Write the one-line pitch for make.fun's "A Day of One-Line Pitches".

Reads MAKEFUN_OUTPUT_DIR (default /output) and writes the single
sentence to entry.txt. Deterministic: no network, no model calls,
no file reads outside the repo.
"""

import os

LINE = (
    "Tell an AI agent your app idea tonight, and wake up to a working "
    "app you can try yourself \u2014 no coding, no cost to start, just "
    "your idea made real on make.fun."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
