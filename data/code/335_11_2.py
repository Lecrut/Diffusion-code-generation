class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if word]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello  world", "Python is great!!! ", "", "   "]
    print(processor.split_sentence("Hello  world"))