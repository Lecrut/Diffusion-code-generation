class TextProcessor:
    @staticmethod
    def extract_first_word(text):
        words = text.split()
        if words:
            return words[0]
        return ""
if __name__ == '__main__':
    sentence1 = "This is a sample sentence."
    sentence2 = "Another test string here."
    sentence3 = "singleword"
    empty_sentence = ""
    print(TextProcessor.extract_first_word(sentence1))
    print(TextProcessor.extract_first_word(sentence2))
    print(TextProcessor.extract_first_word(sentence3))
    print(TextProcessor.extract_first_word(empty_sentence))