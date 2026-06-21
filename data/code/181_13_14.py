import re

class VowelWordFinder:
    def __init__(self):
        self.vowels = set('aeiou')

    def is_vowel_word(self, word):
        return any(char in self.vowels for char in word.lower())

    def find_vowel_words(self, sentence):
        words = re.findall(r'\b\w+\b', sentence.lower())
        vowel_words = [word for word in words if self.is_vowel_word(word)]
        return vowel_words

if __name__ == '__main__':
    finder = VowelWordFinder()
    sample_sentence = "This is a sample sentence with many vowels and consonants."
    result = finder.find_vowel_words(sample_sentence)
    print(result)