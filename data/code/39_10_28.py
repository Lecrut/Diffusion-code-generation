class SubstringExtractor:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def extract_substrings(text, indices):
        substrings = []
        for start, end in indices:
            substrings.append(text[start:end])
        return substrings

if __name__ == '__main__':
    sample_text = "This is a sample string for testing purposes."
    sample_indices = [(0, 4), (10, 15), (30, 40), (5, 7)]
    extractor = SubstringExtractor(sample_text)
    result = SubstringExtractor.extract_substrings(sample_text, sample_indices)
    print(result)