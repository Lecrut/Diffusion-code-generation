class StringUtils:
    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    utils = StringUtils()
    test_strings = ["radar", "hello", "level", "world", "madam"]
    for test in test_strings:
        print(f"'{test}' is a palindrome: {utils.is_palindrome(test)}")