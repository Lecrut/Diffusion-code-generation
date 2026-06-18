class Tokenizer:
    def tokenize(self, sentence: str) -> list[str]:
        return sentence.split()
if __name__ == '__main__':
    sample_sentence = "Hello world this is a test of the tokenizer."
    token_list = Tokenizer().tokenize(sample_sentence)
    print(token_list)