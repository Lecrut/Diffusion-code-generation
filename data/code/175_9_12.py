class SentenceProcessor:
    DEFAULT_DELIMITER = ' '

    @staticmethod
    def split_sentence(sentence):
        return sentence.split(SentenceProcessor.DEFAULT_DELIMITER)

    @staticmethod
    def reverse_words(words):
        return words[::-1]

if __name__ == '__main__':
    processor = SentenceProcessor()
    sample_text = "this is a test string"
    words = processor.split_sentence(sample_text)
    reversed_words = processor.reverse_words(words)
    print(reversed_words)