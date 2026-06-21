class PalindromeChecker:

    def is_palindrome(self, s):
        left, right = (0, len(s) - 1)
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
if __name__ == '__main__':
    checker = PalindromeChecker()
    print(checker.is_palindrome('racecar'))
    print(checker.is_palindrome('hello'))