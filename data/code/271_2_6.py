class PalindromeChecker:
    def __init__(self, text):
        self.text = text

    def clean_text(self):
        return ''.join(char.lower() for char in self.text if char.isalpha())

    def is_palindrome(self):
        cleaned = self.clean_text()
        return cleaned == cleaned[::-1]

if __name__ == '__main__':
    checker = PalindromeChecker("A man, a plan, a canal: Panama")
    print(checker.is_palindrome())
    
    checker = PalindromeChecker("race a car")
    print(checker.is_palindrome())