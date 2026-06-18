class NLPProcessor:
    @staticmethod
    def tokenize(sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    sample_sentence = "The quick brown fox jumps over the lazy dog."
    tokens = NLPProcessor.tokenize(sample_sentence)
    print(tokens)