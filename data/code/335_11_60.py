class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if len(word) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    sample_sentences = ["Hello   world", "Python\nis\tgreat.", "", "Multiple   spaces   and\ntabs"]
    results = [processor.split_sentence(s) for s in sample_sentences]
    print(results)