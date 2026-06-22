class WordExtractor:
    DELIMITER = ' '

    @staticmethod
    def extract_first_word(sentence):
        for index, char in enumerate(sentence):
            if char == WordExtractor.DELIMITER:
                return sentence[:index]
        return sentence

if __name__ == '__main__':
    extractor = WordExtractor()
    print(extractor.extract_first_word("Hello world"))
    print(extractor.extract_first_word("Python programming is fun"))
    print(extractor.extract_first_word("SingleWord"))
    print(extractor.extract_first_word(" "))
    print(extractor.extract_first_word(""))