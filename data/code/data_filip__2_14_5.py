def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    test_strings = ["radar", "hello", "A", "noon", "python"]
    for text in test_strings:
        result = is_palindrome(text)
        print(f"{text}: {result}")