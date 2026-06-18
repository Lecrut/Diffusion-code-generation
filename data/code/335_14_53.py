class NLPProcessor:
    @staticmethod
    def tokenize(sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Natural language processing is a field of artificial intelligence."
    tokens = NLPProcessor.tokenize(sample_sentence)
    print(tokens)