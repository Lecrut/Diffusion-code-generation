class SentenceSplitter:
    def __init__(self):
        pass
    def split_sentence(self, sentence: str) -> list[str]:
        return [word.strip() for word in sentence.split()]
if __name__ == '__main__':
    splitter = SentenceSplitter()
    sample_text = "  Hello   world. This is a test."
    result = splitter.split_sentence(sample_text)
    print(result)