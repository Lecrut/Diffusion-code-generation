class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if len(word) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello   world", "Python\nis\tgreat", "", "Single"]
    results = []
    for s in test_sentences:
        results.append(processor.split_sentence(s))
    print(results)