class WordFinder:
    def __init__(self, text):
        self.text = text

    def find_words_with_substring(self, substring):
        return [word for word in self.text.split() if substring in word]

if __name__ == '__main__':
    finder = WordFinder("Hello world, this is a test string with the substring 'test'.")
    sample_substring = 'test'
    print(finder.find_words_with_substring(sample_substring))