class PalindromeChecker:
    def __init__(self, s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        self.s = s

    def is_palindrome(self):
        left, right = 0, len(self.s) - 1
        while left < right:
            if self.s[left] != self.s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    sample_values = ["racecar", "hello", "madam", "python", "level"]
    for value in sample_values:
        checker = PalindromeChecker(value)
        print(f"'{value}' is a palindrome: {checker.is_palindrome()}")