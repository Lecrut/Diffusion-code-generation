class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if len(word) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    sample_sentences = ["Hello   world", "Python is great!", "", "Multiple   spaces   here"]
    test_cases = []
    for s in sample_sentences:
        result = processor.split_sentence(s)
        test_cases.append((s, result))
    print("Input\tResult")
    for inp, out in test_cases:
        print(f"{repr(inp)}\t{out}")