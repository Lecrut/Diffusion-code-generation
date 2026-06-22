class WordFinder:
    SUBSTRING = 'test'

    @staticmethod
    def find_words_with_substring(text):
        return [word for word in text.split() if WordFinder.SUBSTRING in word]

if __name__ == '__main__':
    sample_text = "Hello world, this is a test string with the substring 'test'."
    result = WordFinder.find_words_with_substring(sample_text)
    print(result)