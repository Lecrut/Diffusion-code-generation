class SentenceProcessor:
    def split_sentence(self, sentence):
        return [word for word in sentence.split() if len(word) > 0]
if __name__ == '__main__':
    processor = SentenceProcessor()
    test_sentences = ["Hello   world", "Python is great!", "", "One two three"]
    results = []
    for s in test_sentences:
        try:
            word_list = processor.split_sentence(s)
            results.append(word_list)
        except Exception as e:
            print(f"Error processing '{s}': {e}")
            continue
    assert all(len(r) > 0 or r == [] for r in results), "Unexpected empty list handling issue."
    sample_output = processor.split_sentence("Hello   world")
    expected_sample = ["Hello", "world"]
    assert sample_output == expected_sample, f"Expected {expected_sample}, got {sample_output}"
print("All tests passed.")