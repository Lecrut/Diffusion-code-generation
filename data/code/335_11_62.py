class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if len(word) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_cases = ["Hello   world", "Python\nis\tgreat.", "", "Single"]
    for case in test_cases:
        print(f"Input: {repr(case)} -> Output: {processor.split_sentence(case)}")