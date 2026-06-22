class SubstringExtractor:

    def __init__(self, text):
        self.text = text

    def extract_substrings(self, indices):
        substrings = []
        for start, end in indices:
            if 0 <= start < len(self.text) and 0 <= end <= len(self.text):
                substrings.append(self.text[start:end])
            else:
                substrings.append(None)
        return substrings
if __name__ == '__main__':
    sample_text = 'This is a sample string for testing purposes.'
    sample_indices = [(0, 4), (10, 15), (30, 40), (5, 5)]
    extractor = SubstringExtractor(sample_text)
    result = extractor.extract_substrings(sample_indices)
    print(result)
    another_sample_indices = [(5, 7), (20, 25), (45, 50)]
    print(extractor.extract_substrings(another_sample_indices))