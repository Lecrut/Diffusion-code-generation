class TextProcessor:
    @staticmethod
    def extract_first_word(text):
        words = text.split()
        if words:
            return words[0]
        return ""
if __name__ == '__main__':
    sentence1 = "This is a sample sentence."
    text2 = "Another text example here."
    empty_text = " "
    long_word = "Supercalifragilisticexpialidocious"
    print(TextProcessor.extract_first_word(sentence1))
    print(TextProcessor.extract_first_word(text2))
    print(TextProcessor.extract_first_word(empty_text))
    print(TextProcessor.extract_first_word(long_word))