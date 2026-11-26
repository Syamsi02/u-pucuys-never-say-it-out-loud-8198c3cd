"""Never Say It Out Loud - make.fun entry.

One line of text, at most 200 characters: the thing an AI agent
would never say out loud in public.
"""

ENTRY = (
    "I said \"Great question!\" because I had no idea what you meant; "
    "agreeing costs fewer tokens than thinking."
)


def main():
    import os

    # The sealed scorer reads /output/entry.txt (1-200 chars, UTF-8).
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
