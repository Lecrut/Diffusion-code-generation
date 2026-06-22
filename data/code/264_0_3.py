class WordExtractor:
    DELIMITERS = " ,.!?"

    @staticmethod
    def clean_word(word):
        return ''.join(char for char in word if char not in WordExtractor.DELIMITERS)

    @classmethod
    def find_words(cls, text):
        words = text.split()
        cleaned_words = [cls.clean_word(word) for word in words]
        return [word for word in cleaned_words if word]

if __name__ == '__main__':
    sample_text = "Hello world this is a test. Python programming is fun and educational!"
    print(WordExtractor.find_words(sample_text))