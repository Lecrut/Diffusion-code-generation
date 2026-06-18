class SentenceProcessor:
    def split_sentence(self, sentence: str) -> list[str]:
        return [word for word in sentence.split() if word]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello  world", "Python   is great!", "", "Multiple   spaces   here"]
    results = []
    for s in test_sentences:
        words = processor.split_sentence(s)
        print(f"Input: '{s}' -> Output: {words}")