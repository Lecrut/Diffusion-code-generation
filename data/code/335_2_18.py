class SentenceSplitter:
    def __init__(self):
        pass
    def split_sentence(self, sentence: str) -> list[str]:
        if not sentence or not isinstance(sentence, str):
            return []
        normalized = " ".join(sentence.split())
        result = [word for word in normalized.strip().split(" ") if word]
        return result
if __name__ == '__main__':
    splitter = SentenceSplitter()
    sample_sentence = "  Hello   world! This is a test.   "
    split_words = splitter.split_sentence(sample_sentence)
    print(split_words)