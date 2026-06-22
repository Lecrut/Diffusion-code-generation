class SubstringExtractor:

    def __init__(self, target_string):
        self.target_string = target_string

    def _generate_substrings(self, k):
        if k <= 0 or k > len(self.target_string):
            return set()
        substrings = set()
        for i in range(len(self.target_string) - k + 1):
            substrings.add(self.target_string[i:i + k])
        return substrings

    def extract_unique_substrings(self, k):
        return self._generate_substrings(k)
if __name__ == '__main__':
    extractor = SubstringExtractor('banana')
    print(extractor.extract_unique_substrings(2))
    print(extractor.extract_unique_substrings(3))
    print(extractor.extract_unique_substrings(4))