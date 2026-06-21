class SentenceProcessor:
    DEFAULT_DELIMITER = ' '

    @staticmethod
    def split_sentence(sentence):
        return sentence.split(SentenceProcessor.DEFAULT_DELIMITER)

    @staticmethod
    def reverse_words(words):
        return words[::-1]

if __name__ == '__main__':
    sample_sentence = "Hello world this is a test"
    processor = SentenceProcessor()
    reversed_words = processor.reverse_words(processor.split_sentence(sample_sentence))
    print(reversed_words)