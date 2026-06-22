class PalindromeFinder:
    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]

    @classmethod
    def find_palindromes(cls, text):
        words = text.split()
        palindromes = [word for word in words if cls.is_palindrome(word)]
        return palindromes

if __name__ == '__main__':
    sample_text = "madam arora teaches malayalam"
    result = PalindromeFinder.find_palindromes(sample_text)
    print(result)