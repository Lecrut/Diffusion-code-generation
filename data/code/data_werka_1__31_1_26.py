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
    sample_values = ["racecar", "hello", "madam", "level", "world"]
    for value in sample_values:
        result = utils.is_palindrome(value)
        print(f"'{value}' is a palindrome: {result}")