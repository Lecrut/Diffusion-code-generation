class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if word]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_cases = ["Hello  world", "No spaces here", "   Leading and trailing   ", "", "Multiple\t\tnot\nspaces"]
    results = []
    for case in test_cases:
        result = processor.split_sentence(case)
        results.append(result)
    expected = [["Hello", "world"], ["No", "spaces", "here"], [], []]