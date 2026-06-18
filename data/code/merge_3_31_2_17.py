def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome ignoring case."""
    return s == s[::-1]

if __name__ == '__main__':
    sample_strings = ["racecar", "hello", "A man, a plan, a canal: Panama"]

    for test_str in sample_strings:
        result = is_palindrome(test_str)
        print(f"Input: '{test_str}'")
        if result:
            print("Result: Palindrome")
        else:
            print("Result: Not a palindrome")