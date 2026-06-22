class PalindromeFinder:
    def find_all_palindromes(self, text):
        words = text.lower().split()
        palindromes = [word for word in words if word == word[::-1] and len(word) > 1]
        return sorted(palindromes)

if __name__ == '__main__':
    finder = PalindromeFinder()
    sample_text = "Able was I ere I saw Elba. Madam In Eden, I'm Adam. Never odd or even."
    result = finder.find_all_palindromes(sample_text)
    print(result)