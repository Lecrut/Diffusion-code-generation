class SentenceProcessor:
    @staticmethod
    def extract_first_word(sentence):
        words = sentence.split()
        return words[0] if words else ""

if __name__ == '__main__':
    sample_sentence = "Hello world from Python"
    processor = SentenceProcessor()
    result = processor.extract_first_word(sample_sentence)
    print(result)