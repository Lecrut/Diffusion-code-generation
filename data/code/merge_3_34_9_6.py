def capitalize_first_letter(text: str) -> str:
    """Capitalizes only the first letter of each word in a string."""
    return text.lower().title()

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "PYTHON IS FUN",
        "multi-word sentence here!",
        "single"
    ]

    results = []
    for s in sample_strings:
        capitalized = capitalize_first_letter(s)
        results.append((s, capitalized))

    # Output the results without using input() or external files
    print("Input -> Output")
    print("-" * 40)
    for original, transformed in results:
        print(f"{original!r} => {transformed!r}")