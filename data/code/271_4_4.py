class WordAnalyzer:
    def __init__(self):
        self.vowels = 'aeiou'

    def count_vowels(self, word):
        return sum(1 for char in word if char.lower() in self.vowels)

    def find_word_with_most_vowels(self, words):
        max_vowel_count = 0
        word_with_max_vowels = ''
        for word in words:
            vowel_count = self.count_vowels(word)
            if vowel_count > max_vowel_count:
                max_vowel_count = vowel_count
                word_with_max_vowels = word
        return word_with_max_vowels

if __name__ == '__main__':
    analyzer = WordAnalyzer()
    sample_words = ['hello', 'world', 'example', 'test']
    print(analyzer.find_word_with_most_vowels(sample_words))