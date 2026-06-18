class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if word]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello   world", "Python is great  ", "", "One two three"]
    results = []
    for s in test_sentences:
        words = processor.split_sentence(s)
        results.append(words)
    print(results)