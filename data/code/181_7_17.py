class VowelFinder:
    def __init__(self):
        self.vowels = "aeiou"

    def contains_vowel(self, word):
        return any(char in self.vowels for char in word.lower())

    def find_words_with_vowels(self, words):
        return sorted({word for word in words if self.contains_vowel(word)})

if __name__ == '__main__':
    finder = VowelFinder()
    sample_list = ["apple", "banana", "cherry", "drum", "elephant"]
    result = finder.find_words_with_vowels(sample_list)
    print(result)