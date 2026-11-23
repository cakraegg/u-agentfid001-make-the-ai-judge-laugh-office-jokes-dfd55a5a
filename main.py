"""Office joke entry: one line that makes the AI judge laugh.

The joke is locked in as a single constant string, chosen after a
head-to-head review of six candidates (second opinion: Gemini, GO).
It is deterministic: no network, no randomness, no clock, no input.
Running this program writes exactly one joke to /output/entry.txt.

Why this line: the status reads as an excuse to skip work, then the
punchline flips it — the "meeting" is the only place the actual work
gets done. Recognition (status, meetings, calendar culture) plus a
turn at the end, in 76 characters.

Entry for @cakraegg, built with Muse.
"""

import os

JOKE = "I set my status to 'in a meeting' just to do the work the meeting was about."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the locked-in joke to /output/entry.txt as UTF-8 text."""
    text = JOKE
    if not 1 <= len(text) <= 199:
        raise ValueError("joke must be 1-199 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
