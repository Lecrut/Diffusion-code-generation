def reverse_string(s: str) -> str:
    """Reverses the order of characters in the input string."""
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    test_cases = [
        "Hello, World!",
        "",
        "Python",
        "!@#$%",
        "A man a plan a canal Panama"
    ]

    for original in test_cases:
        reversed_str = reverse_string(original)
        print(f"Original:  '{original}'")
        print(f"Reversed:  '{reversed_str}'")
        print("-" * 30)