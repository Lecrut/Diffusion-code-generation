class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if word]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello   world", "Python is great  ", "", "One two three"]
    results = []
    for s in test_sentences:
        results.append(processor.split_sentence(s))
    print(results)