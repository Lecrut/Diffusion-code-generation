class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if len(word) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    sample_sentences = [
        "Hello   world",
        "Python is great!",
        "",
        "Multiple   spaces   and   punctuation"
    ]
    for s in sample_sentences:
        result = processor.split_sentence(s)
        print(result)