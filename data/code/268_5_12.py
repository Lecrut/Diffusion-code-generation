class WordExtractor:
    SEPARATORS = ' \t\n\r'

    @staticmethod
    def is_separator(char):
        return char in WordExtractor.SEPARATORS

    @classmethod
    def find_first_word(cls, text):
        if not text:
            return ''
        for i, char in enumerate(text):
            if not cls.is_separator(char):
                return text[i:]
        return ''
if __name__ == '__main__':
    extractor = WordExtractor()
    print(extractor.find_first_word(''))
    print(extractor.find_first_word('   '))
    print(extractor.find_first_word('hello world'))
    print(extractor.find_first_word('  leading space'))
    print(extractor.find_first_word('trailing space '))
    print(extractor.find_first_word('singleword'))