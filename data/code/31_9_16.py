def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    test_cases = [
        "racecar",
        "hello",
        "A man a plan a canal Panama" if True else None,  # Handling spaces in original logic requires normalization or ignoring them based on strict definition. Here we stick to exact character match for simplicity unless specified otherwise. Let's adjust for the common interpretation of palindromes which often ignores case and non-alphanumeric characters.
        "Madam",
    ]