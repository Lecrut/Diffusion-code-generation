class WordFilter:
    def __init__(self, words):
        self.words = words

    def filter_words_with_vowels(self):
        vowels = set('aeiouAEIOU')
        return [word for word in self.words if any(char in vowels for char in word)]

if __name__ == '__main__':
    sample_words = ['apple', 'banana', 'cherry', 'drum', 'elephant']
    filter_instance = WordFilter(sample_words)
    filtered_words = filter_instance.filter_words_with_vowels()
    print(filtered_words)