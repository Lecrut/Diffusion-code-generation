class WordExtractor:
    @staticmethod
    def get_first_word(text):
        words = text.split()
        if words:
            return words[0]
        else:
            return ""

if __name__ == '__main__':
    extractor = WordExtractor()
    print(extractor.get_first_word("Hello world"))
    print(extractor.get_first_word("   leading spaces and multiple words"))
    print(extractor.get_first_word(""))
    print(extractor.get_first_word("singleword"))
    print(extractor.get_first_word("  "))