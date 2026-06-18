def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome, ignoring case."""
    return s == s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to run without user input
    samples = ["racecar", "hello", "A man a plan a canal Panama"]

    for text in samples:
        result = is_palindrome(text)
        print(f"Input: '{text}'")
        if result:
            print("Result: Palindrome")
        else:
            print("Result: Not a palindrome")