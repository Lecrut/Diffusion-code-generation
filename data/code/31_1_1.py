class StringUtils:
    def is_palindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        return True
if __name__ == '__main__':
    utils = StringUtils()
    test_strings = [
        "racecar",
        "hello",
        "madam",
        "a",
        "noon",
        "abcde",
        "",
        "level"
    ]
    for s in test_strings:
        result = utils.is_palindrome(s)
        print(f"'{s}' is a palindrome: {result}")