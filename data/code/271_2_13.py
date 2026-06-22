class PalindromeChecker:
    def __init__(self, text):
        self.text = text

    def is_palindrome(self):
        cleaned_text = ''.join(char.lower() for char in self.text if char.isalpha())
        return cleaned_text == cleaned_text[::-1]

if __name__ == '__main__':
    checker1 = PalindromeChecker("A man, a plan, a canal: Panama")
    print(checker1.is_palindrome())

    checker2 = PalindromeChecker("race a car")
    print(checker2.is_palindrome())