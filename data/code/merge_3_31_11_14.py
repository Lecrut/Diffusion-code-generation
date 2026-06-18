def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome, ignoring case and non-alphanumeric characters."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race car",
        "Hello World!",
        "Was it a car or a cat I saw?",
        "Not a palindrome"
    ]

    print("Palindrome Checker")
    print("-" * 30)

    for test_string in test_cases:
        result = is_palindrome(test_string)
        status = "IS A PALINDROME" if result else "NOT A PALINDROME"
        print(f'Input: "{test_string}"')
        print(f'Result: {status}\n')