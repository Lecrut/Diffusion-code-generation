class WordProcessor:
    @staticmethod
    def get_first_word(text):
        words = text.split()
        if words:
            return words[0]
        else:
            return ""

if __name__ == '__main__':
    processor = WordProcessor()
    print(processor.get_first_word("Hello world"))
    print(processor.get_first_word("  leading spaces and multiple words "))
    print(processor.get_first_word(""))
    print(processor.get_first_word("singleword"))
    print(processor.get_first_word("   "))