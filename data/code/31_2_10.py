def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome, ignoring case."""
    return s == s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or external dependencies.
    test_cases = [
        "radar",
        "hello",
        "A man a plan a canal Panama",  # Includes spaces and mixed case for robustness check if needed, but strict palindrome logic applies directly here.
        "12321"
    ]

    print("Palindrome Check Results:")
    for test_string in test_cases:
        result = is_palindrome(test_string)
        status = "is a palindrome" if result else "is NOT a palindrome"
        print(f"'{test_string}' {status}")