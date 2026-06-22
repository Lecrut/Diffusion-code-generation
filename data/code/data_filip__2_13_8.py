def is_palindrome(s: str) -> bool:
    return s == s[::-1]

if __name__ == '__main__':
    test_strings = ["racecar", "hello", "Madam", "12321", "python"]
    for text in test_strings:
        result = is_palindrome(text)
        print(f"{text}: {result}")