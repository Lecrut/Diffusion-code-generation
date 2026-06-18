class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Natural language processing is the science of enabling computers to understand human language."
    tokens = NLPProcessor().tokenize(sample_sentence)
    print(tokens)