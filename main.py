"""Autocorrect-fail entry runner.

Loads the single-line joke from entry.txt, makes sure it fits the
bounty's shape (exactly one line, 1 to 199 characters), hands it to
the grader at /output/entry.txt, and echoes it to stdout.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.txt"
TARGET = Path("/output/entry.txt")
CHAR_LIMIT = 199


def fetch_line():
    raw = SOURCE.read_text(encoding="utf-8")
    stripped = raw.strip()
    if not stripped:
        raise SystemExit("entry.txt holds no text")
    if "\n" in stripped:
        raise SystemExit("entry must be a single line")
    if len(stripped) > CHAR_LIMIT:
        raise SystemExit(
            f"entry is {len(stripped)} chars, limit is {CHAR_LIMIT}"
        )
    return stripped


def deliver(text):
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    if TARGET.read_text(encoding="utf-8").strip() != text:
        raise SystemExit("written entry did not round-trip cleanly")
    print(text)


if __name__ == "__main__":
    deliver(fetch_line())
