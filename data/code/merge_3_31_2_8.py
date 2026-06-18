def is_palindrome(s):
    """Check if a string is a palindrome ignoring spaces, punctuation, and case."""
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "Race car!",
        "Hello World",
        "Was it a cat and I saw a cat?",
        ""
    ]

    for test_str in sample_strings:
        result = is_palindrome(test_str)
        print(f"Input: '{test_str}'")
        if result:
            print("Result: The string is a palindrome.")
        else:
            print("Result: The string is NOT a palindrome.")