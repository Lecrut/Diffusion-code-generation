class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if len(word) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_cases = ["Hello   world", "One two three ", "", "Multiple   spaces   here"]
    for case in test_cases:
        print(processor.split_sentence(case))