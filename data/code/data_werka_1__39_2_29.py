class SubstringExtractor:
    def __init__(self):
        self.substrings = set()

    def add_substring(self, substring: str):
        self.substrings.add(substring)

    def extract_unique_substrings(self, s: str, k: int) -> set:
        if k <= 0 or k > len(s):
            return set()
        
        for i in range(len(s) - k + 1):
            substring = s[i:i+k]
            self.add_substring(substring)
        
        return self.substrings

if __name__ == '__main__':
    extractor = SubstringExtractor()
    target_string = "abacabad"
    substring_length = 3
    result = extractor.extract_unique_substrings(target_string, substring_length)
    print(result)