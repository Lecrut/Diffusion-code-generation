class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if word]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello   world", "Python\nis\nawesome", "", "  Multiple   spaces  here  "]
    for s in test_sentences:
        result = processor.split_sentence(s)
        print(result)