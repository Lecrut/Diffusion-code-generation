class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if len(word) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello   world", "Python is great.", "", "Multiple   spaces  and tabs\t"]
    results = []
    for s in test_sentences:
        result = processor.split_sentence(s)
        results.append(f"Input: {repr(s)} -> Output: {result}")
    print("\n".join(results))