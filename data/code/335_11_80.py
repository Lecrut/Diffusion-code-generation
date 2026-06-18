class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if word]
if __name__ == '__main__':
    processor = SentenceProcessor()
    sample_sentences = ["Hello  world", "Python   is great!!", ""]
    results = []
    for s in sample_sentences:
        words = processor.split_sentence(s)
        results.append(words)
    print(results)