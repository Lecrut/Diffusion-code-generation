class PalindromeChecker:
    def __init__(self, text):
        self.text = text

    def is_palindrome(self):
        filtered_chars = [char.lower() for char in self.text if char.isalpha()]
        return filtered_chars == filtered_chars[::-1]

if __name__ == '__main__':
    checker = PalindromeChecker("A man, a plan, a canal: Panama")
    print(checker.is_palindrome())
    checker = PalindromeChecker("race a car")
    print(checker.is_palindrome())