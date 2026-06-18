def reverse_word(text: str) -> str:
    """Return the input string with characters reversed."""
    return text[::-1]

if __name__ == '__main__':
    samples = [
        "hello",
        "Python Programming",
        "",
        "a"
    ]

    for sample in samples:
        print(f"Original: {sample!r}")