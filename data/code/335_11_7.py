class SentenceProcessor:
    def __init__(self):
        pass
    def split_sentence(self, sentence: str) -> list[str]:
        return [word for word in sentence.split() if len(word.strip()) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello   world", "Python\nis\tawesome", "", "Multiple   spaces"]
    results = []
    for s in test_sentences:
        words = processor.split_sentence(s)
        results.append(words)
    print(results)