class PalindromeChecker:
    def __init__(self, text):
        self.text = text

    def is_palindrome(self):
        return self.text == self.text[::-1]

if __name__ == '__main__':
    checker1 = PalindromeChecker("racecar")
    print(checker1.is_palindrome())
    checker2 = PalindromeChecker("hello")
    print(checker2.is_palindrome())
    checker3 = PalindromeChecker("Level")
    print(checker3.is_palindrome())
    checker4 = PalindromeChecker("12321")
    print(checker4.is_palindrome())