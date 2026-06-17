class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if len(word) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello   world", "Python is great\nand fun.", "", "One"]
    results = []
    for s in test_sentences:
        word_list = processor.split_sentence(s)
        results.append(word_list)
    print(results)