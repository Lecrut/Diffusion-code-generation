class SubstringExtractor:
    def extract_unique_substrings(self, s: str, k: int) -> set:
        if k <= 0 or k > len(s):
            return set()
        substrings = set()
        for i in range(len(s) - k + 1):
            substrings.add(s[i:i+k])
        return substrings
if __name__ == '__main__':
    extractor = SubstringExtractor()
    target_string = "ababa"
    substring_length = 3
    result = extractor.extract_unique_substrings(target_string, substring_length)
    print(result)