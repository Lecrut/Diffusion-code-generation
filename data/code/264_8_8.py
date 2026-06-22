class WordFinder:
    def __init__(self, text):
        self.text = text.split()

    def find_words_with_substring(self, substring):
        return [word for word in self.text if substring in word]

if __name__ == '__main__':
    sample_text = "Hello world, this is a test string with the substring 'test'."
    sample_substring = 'test'
    finder = WordFinder(sample_text)
    result = finder.find_words_with_substring(sample_substring)
    print(result)