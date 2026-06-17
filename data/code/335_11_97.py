class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if len(word) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello   world", "Python is\tgreat\nand fast.", "", "   "]
    for s in test_sentences:
        print(processor.split_sentence(s))