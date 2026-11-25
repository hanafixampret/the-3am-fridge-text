"""The 3AM Fridge Text: one line a smart fridge texts its owner at 3am."""

LINE = "3am. You stare into me like I have answers. I have condiments and regret. Pick one."

# The gate allows 1-140 characters; the line is one lock-screen text, no follow-up.
assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
