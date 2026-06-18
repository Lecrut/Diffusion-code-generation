def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome, ignoring case and non-alphanumeric characters."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
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
        status = "Is a palindrome!" if result else "Is NOT a palindrome."
        print(f'Input: "{test_string}"')
        print(status)
        print("-" * 30)