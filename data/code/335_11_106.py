class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if len(word) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello world", "   Multiple      spaces  ", "", "One"]
    results = []
    for sent in test_sentences:
        result = processor.split_sentence(sent)
        results.append(result)
    assert results[0] == ['Hello', 'world']
    assert results[1] == ['Multiple', 'spaces']
    assert results[2] == []
    assert results[3] == ['One']
    print("All tests passed.")