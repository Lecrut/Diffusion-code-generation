def reverse_word(s: str) -> str:
    """Returns a new string with characters in 's' reversed."""
    return s[::-1]

if __name__ == '__main__':
    test_cases = [
        "hello",
        "Pythonic approach is best.",
        "",
        "a"
    ]

    for word in test_cases:
        print(f"{word} -> {reverse_word(word)}")