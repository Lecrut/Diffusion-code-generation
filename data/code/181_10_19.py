class WordFilter:
    def __init__(self):
        self.vowels = set('aeiouAEIOU')

    def contains_vowel(self, word):
        return any(char in self.vowels for char in word)

    def filter_words(self, words):
        return [word for word in words if self.contains_vowel(word)]

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry', 'drum', 'elephant']
    filter_instance = WordFilter()
    filtered_words = filter_instance.filter_words(sample_words)
    print(filtered_words)