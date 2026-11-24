"""Write one fortune-cookie line for a developer to /output/entry.txt.

The line is a single original fortune-cookie sentence (105 characters):
kindness toward the stranger who wrote the legacy code you curse, with
the twist that the stranger was you, at 2 a.m. yesterday.

Deterministic: no network, no clock, no randomness, no reads outside
this repository. The grader runs it twice; both runs write byte-identical
output.
"""

import os

ENTRY = (
    "Be kind to the stranger who wrote the legacy code you curse "
    "\u2014 at 2 a.m. yesterday, that stranger was you."
)


def validate_entry(text: str) -> str:
    """Check the entry against the bounty gate; fail loudly if it breaks.

    Gate: UTF-8 text of 1 to 120 characters, not only whitespace.
    The entry must also be a single line ending in sentence punctuation.
    Note "2 a.m." contains a period, so a sentence split is detected by a
    terminator followed by a space only after expanding the abbreviation.
    """
    entry = text.strip()
    if not entry:
        raise SystemExit("entry is empty or only whitespace")
    if len(entry) > 120:
        raise SystemExit(
            f"entry is {len(entry)} characters, over the 120-character limit"
        )
    if "\n" in entry or "\r" in entry:
        raise SystemExit("entry must be a single line")
    if entry[-1] not in ".!?":
        raise SystemExit("entry must end with sentence-ending punctuation")
    probe = entry.replace("a.m.", "am").replace("p.m.", "pm")
    for sep in (". ", "! ", "? "):
        if sep in probe:
            raise SystemExit(f"entry contains more than one sentence ({sep!r})")
    return entry


def main() -> None:
    entry = validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
