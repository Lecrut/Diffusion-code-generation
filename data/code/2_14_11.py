def is_palindrome(s: str) -> bool:
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    test_strings = ["racecar", "hello", "madam", "a"]
    results = [is_palindrome(s) for s in test_strings]
    print(results)