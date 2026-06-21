class WordExtractor:
    DELIMITERS = ',.?!'

    @staticmethod
    def extract_words(sentence):
        return [word.strip(WordExtractor.DELIMITERS) for word in sentence.split(',') if word]

if __name__ == '__main__':
    phrase = "apple,banana,,orange,,,,"
    words = WordExtractor.extract_words(phrase)
    print(words)