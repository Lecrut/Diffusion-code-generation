def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome, ignoring case and non-alphanumeric characters."""
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    sample_cases = [
        "A man, a plan, a canal: Panama",
        "Race car",
        "Hello World!",
        "Was it a car or a cat I saw?",
        "Madam"
    ]

    for test_string in sample_cases:
        result = is_palindrome(test_string)
        print(f"'{test_string}' -> Palindrome: {'Yes' if result else 'No'}")