class Tokenizer:
    def tokenize(self, sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    tokenizer = Tokenizer()
    sample_sentence = "Natural language processing is a fascinating field."
    tokens = tokenizer.tokenize(sample_sentence)