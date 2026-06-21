class WordFinder:
    @staticmethod
    def is_alphabetic(word):
        return word.isalpha()

    @classmethod
    def find_alphabetic_words(cls, text):
        return [word for word in text.split() if cls.is_alphabetic(word)]

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test."
    print(WordFinder.find_alphabetic_words(sample_text))