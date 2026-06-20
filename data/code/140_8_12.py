class PalindromeChecker:

    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]
if __name__ == '__main__':
    test_string = 'racecar'
    result = PalindromeChecker.is_palindrome(test_string)
    print(result)