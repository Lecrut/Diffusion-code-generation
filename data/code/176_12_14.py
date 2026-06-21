class WordExtractor:
    @staticmethod
    def extract_alphabetic_words(text):
        return [word for word in text.split() if word.isalpha()]

if __name__ == '__main__':
    sample_text = "Hello, world! This is a test."
    alphabetic_words = WordExtractor.extract_alphabetic_words(sample_text)
    print(alphabetic_words)