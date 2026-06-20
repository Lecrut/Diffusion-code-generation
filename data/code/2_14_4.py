def is_palindrome(s: str) -> bool:
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    test_strings = ["racecar", "hello", "Able was I ere I saw Elba", "12321", "12345"]
    for text in test_strings:
        print(is_palindrome(text))