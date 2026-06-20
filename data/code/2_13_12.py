def is_palindrome(text: str) -> bool:
    return text == text[::-1]

if __name__ == '__main__':
    test_cases = ["radar", "hello", "A man a plan a canal Panama", "12321", "12345"]
    for value in test_cases:
        print(is_palindrome(value))