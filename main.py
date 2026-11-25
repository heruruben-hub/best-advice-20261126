"""Write the best-advice entry to /output/entry.txt.

The entry is one sentence (161 characters) about the best advice the
writer ever received, from his grandfather: never trust a man who will
not look you in the eye when he shakes your hand, verified over thirty
years of meeting people. The gate requires UTF-8 text of 1 to 200
characters, not only white space, written to /output/entry.txt.
"""

import os

ENTRY = (
    "My grandfather said never to trust a man who won't look you in "
    "the eye when he shakes your hand, and in thirty years I have yet "
    "to meet one who proved him wrong."
)

OUTPUT_PATH = "/output/entry.txt"


def _validate(text: str) -> str:
    """Check the entry against the gate: 1-200 chars, not only white space."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, gate needs 1-200")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    return text


def main() -> None:
    entry = _validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    _validate(written)
    if written != entry:
        raise ValueError("round-trip check failed: file differs from entry")


if __name__ == "__main__":
    main()
