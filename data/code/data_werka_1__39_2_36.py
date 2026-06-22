class SubstringExtractor:

    def __init__(self, text):
        self.text = text

    def _generate_substrings(self, k):
        substrings = set()
        for i in range(len(self.text) - k + 1):
            substrings.add(self.text[i:i + k])
        return substrings

    def extract_unique_substrings(self, k):
        if k <= 0 or k > len(self.text):
            return set()
        return self._generate_substrings(k)
if __name__ == '__main__':
    extractor = SubstringExtractor('banana')
    print(extractor.extract_unique_substrings(2))
    print(extractor.extract_unique_substrings(3))
    print(extractor.extract_unique_substrings(4))