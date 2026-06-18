def reverse_word(s: str) -> str:
    """Returns a new string with characters in 's' reversed."""
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_cases = [
        "hello",
        "Pythonic solution for reversing strings.",
        "",
        "a",
        "racecar"
    ]

    print("Input -> Output")
    print("-" * 30)
    
    for word in test_cases:
        reversed_word = reverse_word(word)
        print(f"{word!r} -> {reversed_word!r}")