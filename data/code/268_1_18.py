class TextProcessor:
    EMPTY_STRING = ""

    @staticmethod
    def get_first_word(text):
        words = text.split()
        return words[0] if words else TextProcessor.EMPTY_STRING

if __name__ == '__main__':
    processor = TextProcessor()
    print(processor.get_first_word("Hello world"))
    print(processor.get_first_word("   leading spaces and multiple words"))
    print(processor.get_first_word(""))
    print(processor.get_first_word("singleword"))
    print(processor.get_first_word(""))
    print(processor.get_first_word(""))