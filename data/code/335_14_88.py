class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Natural language processing is a fascinating field."
    tokens = NLPProcessor().tokenize(sample_sentence)
    print(tokens)