class SubstringExtractor:
    def extract_unique_substrings(self, text: str, k: int) -> set:
        if k <= 0 or k > len(text):
            return set()
        substrings = set()
        n = len(text)
        for i in range(n - k + 1):
            substrings.add(text[i:i+k])
        return substrings
if __name__ == '__main__':
    extractor = SubstringExtractor()
    target_string = "ababa"
    substring_length = 3
    result = extractor.extract_unique_substrings(target_string, substring_length)
    print(result)