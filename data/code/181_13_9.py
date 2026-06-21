class VowelWordFinder:
    def __init__(self):
        self.vowels = set("aeiou")

    def has_vowel(self, word):
        return any(char in self.vowels for char in word.lower())

    def find_vowel_words(self, sentence):
        words = sentence.split()
        return [word for word in words if self.has_vowel(word)]

if __name__ == '__main__':
    finder = VowelWordFinder()
    sample_sentence = "This is a sample sentence with many vowels and consonants."
    result = finder.find_vowel_words(sample_sentence)
    print(result)