class PalindromeDetector:
    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]

    @staticmethod
    def find_palindromes(text):
        words = text.split()
        palindromes = [word for word in words if PalindromeDetector.is_palindrome(word)]
        return palindromes

if __name__ == '__main__':
    sample_text = "madam arora teaches malayalam"
    detector = PalindromeDetector()
    result = detector.find_palindromes(sample_text)
    print(result)