class StringUtils:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    sample_strings = ["racecar", "hello", "level", "world", "madam"]
    for string in sample_strings:
        print(f"'{string}' is a palindrome: {StringUtils.is_palindrome(string)}")