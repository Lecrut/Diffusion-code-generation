class PalindromeFinder:
    def find_palindromes(self, text):
        words = text.lower().split()
        palindromes = [word for word in words if word == word[::-1] and len(word) > 1]
        return sorted(list(set(palindromes)))

if __name__ == '__main__':
    finder = PalindromeFinder()
    sample_text = "Madam Arora teaches malayalam. Did Hannah see Elba?"
    result = finder.find_palindromes(sample_text)
    print(result)