class PalindromeFinder:
    def find_palindromes(self, text):
        words = text.split()
        palindromes = [word for word in words if word == word[::-1]]
        return palindromes

if __name__ == '__main__':
    sample_text = "madam arora teaches malayalam"
    finder = PalindromeFinder()
    result = finder.find_palindromes(sample_text)
    print(result)