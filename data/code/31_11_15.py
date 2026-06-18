def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome, ignoring case and non-alphanumeric characters."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without user input or external dependencies.
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "race car",
        "Hello World!",
        "Was it a car or a cat I saw?",
        "Not a palindrome"
    ]

    print("Palindrome Checker")
    print("-" * 30)

    for test_string in sample_strings:
        result = is_palindrome(test_string)
        status = "IS A PALINDROME" if result else "NOT A PALINDROME"
        print(f'Input: "{test_string}"')
        print(f'Result: {status}\n')

    # Additional interactive-style simulation using hardcoded values to mimic user prompts.
    test_cases = [
        ("Madam", True),
        ("Python 3.12", False)
    ]

    for input_str, expected in test_cases:
        actual_result = is_palindrome(input_str)
        match_status = "Match" if actual_result == expected else "Mismatch (Unexpected)"
        print(f'Testing "{input_str}": Expected {expected}, Got {actual_result}. Status: {match_status}')