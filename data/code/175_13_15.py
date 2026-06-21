class SentenceSplitter:
    _DEFAULT_SENTENCE = "  Hello world!   This is a test sentence with various spaces. "
    
    @staticmethod
    def split(sentence=_DEFAULT_SENTENCE):
        return sentence.split()

if __name__ == '__main__':
    words = SentenceSplitter.split()
    print(words)