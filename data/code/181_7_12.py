class VowelWordFinder:
    def __init__(self):
        self.vowels = {'a', 'e', 'i', 'o', 'u'}

    def has_vowel(self, word):
        return any(char in self.vowels for char in word.lower())

    def find_words_with_vowels(self, words):
        return sorted(word for word in words if self.has_vowel(word))

if __name__ == '__main__':
    finder = VowelWordFinder()
    sample_words = ["apple", "banana", "cherry", "drum", "elephant"]
    result = finder.find_words_with_vowels(sample_words)
    print(result)