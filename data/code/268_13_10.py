class SentenceProcessor:
    DELIMITER = ' '

    @staticmethod
    def extract_first_word(sentence):
        word = ''
        for char in sentence:
            if char == SentenceProcessor.DELIMITER:
                break
            word += char
        return word

if __name__ == '__main__':
    sample_sentence = "Hello, world!"
    processor = SentenceProcessor()
    print(processor.extract_first_word(sample_sentence))