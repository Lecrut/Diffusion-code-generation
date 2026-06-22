class SubstringExtractor:
    def __init__(self):
        self._substrings = set()

    def extract_unique_substrings(self, s: str, k: int) -> set:
        if k <= 0 or k > len(s):
            return set()
        
        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            self._substrings.add(substring)
        
        return self._substrings

if __name__ == '__main__':
    extractor = SubstringExtractor()
    target_string = "hello world"
    substring_length = 4
    unique_substrings = extractor.extract_unique_substrings(target_string, substring_length)
    print(unique_substrings)