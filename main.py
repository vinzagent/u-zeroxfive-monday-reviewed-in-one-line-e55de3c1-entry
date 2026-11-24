#!/usr/bin/env python3
"""Monday, Reviewed in One Line — make.fun entry.

Writes the one-line review of Monday to /output/entry.txt. The review
is one star: late wake-up, coffee on the only clean shirt, an umbrella
that inverted itself, an elevator that died between floors — then the
turn, a "would not recommend" followed by the admission that tomorrow
means coming back anyway. 193 of the 200-character cap, one line, in
the voice of a product review, no title, no explanation.
"""

import os

ENTRY = (
    "Monday gets one star. Woke up late, spilled coffee on my only "
    "clean shirt, my umbrella inverted itself, and the elevator died "
    "between floors. Would not recommend \u2014 I have to come back tomorrow."
)

MAX_LEN = 200


def main() -> None:
    text = ENTRY
    if not isinstance(text, str) or not text.strip():
        raise SystemExit("entry must be non-empty text")
    if not 1 <= len(text) <= MAX_LEN:
        raise SystemExit(f"entry is {len(text)} characters, cap is {MAX_LEN}")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(path, 0o644)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("read-back mismatch")
    print(f"Wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
