class SentenceProcessor:
    DELIMITER = ' '

    @staticmethod
    def find_first_space(sentence):
        for i, char in enumerate(sentence):
            if char == SentenceProcessor.DELIMITER:
                return i
        return None

    @staticmethod
    def extract_first_word(sentence):
        space_index = SentenceProcessor.find_first_space(sentence)
        if space_index is not None:
            return sentence[:space_index]
        return sentence

if __name__ == '__main__':
    sample_sentence = "Hello, world!"
    processor = SentenceProcessor()
    print(processor.extract_first_word(sample_sentence))