class StringUtils:
    def is_palindrome_inplace(self, s: str) -> bool:
        if not s:
            return True
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
if __name__ == '__main__':
    utils = StringUtils()
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("", True),
        ("a", True),
        ("abba", True),
        ("abcba", True),
        ("abc", False),
        ("madam", True)
    ]
    for s, expected in test_cases:
        result = utils.is_palindrome_inplace(s)
        print(f"Input: '{s}', Expected: {expected}, Got: {result}, Match: {result == expected}")