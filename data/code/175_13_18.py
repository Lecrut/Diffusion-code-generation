class SentenceSplitter:
    def __init__(self):
        self.SPLIT_PATTERN = r'\b\w+\b'

    @staticmethod
    def split_sentence(sentence):
        return re.findall(SentenceSplitter.SPLIT_PATTERN, sentence)

if __name__ == '__main__':
    splitter = SentenceSplitter()
    sample_sentence = "  Hello   world! This is a test sentence. "
    words = splitter.split_sentence(sample_sentence)
    print(words)