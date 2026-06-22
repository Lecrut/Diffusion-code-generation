class PalindromeDetector:
    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]

    def detect_palindromes(self, text):
        words = text.split()
        palindromes = [word for word in words if self.is_palindrome(word)]
        return palindromes

if __name__ == '__main__':
    sample_text = "madam arora teaches malayalam"
    detector = PalindromeDetector()
    result = detector.detect_palindromes(sample_text)
    print(result)