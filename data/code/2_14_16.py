def is_palindrome(s):
    if not isinstance(s, str):
        return False
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    test_strings = ["racecar", "hello", "madam", "python", "a"]
    for s in test_strings:
        result = is_palindrome(s)
        print(result)