class SubstringExtractor:
    MAX_SUBSTRING_LENGTH = 100

    @staticmethod
    def is_valid_length(k: int, s: str) -> bool:
        return 0 < k <= len(s) and k <= SubstringExtractor.MAX_SUBSTRING_LENGTH

    def extract_unique_substrings(self, s: str, k: int) -> set:
        if not SubstringExtractor.is_valid_length(k, s):
            return set()
        
        substrings = set()
        for i in range(len(s) - k + 1):
            substrings.add(s[i:i+k])
        return substrings

if __name__ == '__main__':
    extractor = SubstringExtractor()
    target_string = "abacabad"
    substring_length = 3
    result = extractor.extract_unique_substrings(target_string, substring_length)
    print(result)