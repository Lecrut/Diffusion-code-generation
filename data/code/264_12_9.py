class PalindromeFinder:
    PUNCTUATION = set("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

    @staticmethod
    def is_palindrome(word):
        cleaned_word = ''.join(char for char in word if char.isalnum()).lower()
        return cleaned_word == cleaned_word[::-1]

    def find_all_palindromes(self, text):
        words = text.split()
        palindromes = [word for word in words if self.is_palindrome(word)]
        return sorted(palindromes)

if __name__ == '__main__':
    finder = PalindromeFinder()
    sample_text = "Madam Arora teaches malayalam. Did you see a car or a cat I saw?"
    result = finder.find_all_palindromes(sample_text)
    print(result)