class NLPProcessor:
    def tokenize(self, sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    processor = NLPProcessor()
    sample_sentence = "Natural language processing is the simulation of human intelligence in computer systems."
    tokens = processor.tokenize(sample_sentence)
    print(tokens)