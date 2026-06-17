class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word.strip() for word in sentence.split() if word]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello  world", "Python   is great!", "SingleWord"]
    results = []
    for s in test_sentences:
        words = processor.split_sentence(s)
        results.append(words)
    print(results)