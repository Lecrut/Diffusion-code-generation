def get_first_letter(text: str) -> str:
    """Returns the first letter of the input string if it exists, otherwise an empty string."""
    return text[0] if len(text) > 0 else ""

if __name__ == '__main__':
    sample_strings = [
        "Hello World",
        "",
        "!@#123",
        "a"
    ]

    for s in sample_strings:
        print(f'Input "{s}" -> Output "{get_first_letter(s)}"')