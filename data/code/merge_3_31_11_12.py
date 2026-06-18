import string

def is_palindrome(s: str) -> bool:
    """Check if a given string is a palindrome, ignoring case and non-alphanumeric characters."""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "race car",
        "hello world"
    ]

    for test_str in sample_strings:
        result = is_palindrome(test_str)
        print(f"'{test_str}' -> {'Palindrome' if result else 'Not a palindrome'}")