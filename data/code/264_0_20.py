class WordProcessor:
    DELIMITERS = " ,.!?"

    @staticmethod
    def clean_word(word):
        return ''.join(char for char in word if char not in WordProcessor.DELIMITERS)

    @classmethod
    def find_words(cls, text):
        words = text.split()
        cleaned_words = [cls.clean_word(word) for word in words]
        return [word for word in cleaned_words if word]

if __name__ == '__main__':
    extractor = WordProcessor()
    sample_text = "Hello world this is a test. Python programming is fun and educational!"
    result = extractor.find_words(sample_text)
    print(result)