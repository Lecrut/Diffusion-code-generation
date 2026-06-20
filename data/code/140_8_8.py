class PalindromeChecker:
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

if __name__ == '__main__':
    test_strings = ["racecar", "hello", "level", "world"]
    for string in test_strings:
        print(f"'{string}' is palindrome: {PalindromeChecker.is_palindrome(string)}")