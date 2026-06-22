class WordProcessor:
    def __init__(self, text):
        self.text = text

    def get_first_word(self):
        words = self.text.split()
        if words:
            return words[0]
        else:
            return ""

if __name__ == '__main__':
    processor1 = WordProcessor("Hello world")
    print(processor1.get_first_word())

    processor2 = WordProcessor("   leading spaces and multiple words")
    print(processor2.get_first_word())

    processor3 = WordProcessor("singleword")
    print(processor3.get_first_word())

    processor4 = WordProcessor("")
    print(processor4.get_first_word())