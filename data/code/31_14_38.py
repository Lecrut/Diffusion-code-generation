class PalindromeChecker:
    def __init__(self, string):
        self.string = string

    def is_palindrome(self) -> bool:
        left, right = 0, len(self.string) - 1
        while left < right:
            if self.string[left] != self.string[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == '__main__':
    sample_values = ["racecar", "hello", "madam", "python", "level"]
    for value in sample_values:
        checker = PalindromeChecker(value)
        print(f"'{value}' is a palindrome: {checker.is_palindrome()}")