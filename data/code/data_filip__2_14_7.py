def is_palindrome(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

if __name__ == '__main__':
    sample_strings = [
        "racecar",
        "hello",
        "madam",
        "python",
        "a",
        ""
    ]
    for s in sample_strings:
        result = is_palindrome(s)
        print(result)