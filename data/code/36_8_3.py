def reverse_string_recursive(s: str) -> str:
    """Recursively reverses a string."""
    if len(s) <= 1:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies.
    test_cases = [
        "hello",
        "",
        "a",
        "Python Programming"
    ]

    for text in test_cases:
        reversed_text_recursive = reverse_string_recursive(text)
        print(f"Original: {text}")
        print(f"Reversed (Recursive): {reversed_text_recursive}\n")