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
    util = StringUtils()
    sample_strings = ["racecar", "hello", "madam", "world"]
    for string in sample_strings:
        print(f"'{string}' is a palindrome: {util.is_palindrome(string)}")