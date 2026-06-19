class SubstringExtractor:
    def __init__(self, target_string: str):
        self.target_string = target_string

    def _validate_length(self, k: int) -> bool:
        return 0 < k <= len(self.target_string)

    def extract_unique_substrings(self, k: int) -> set:
        if not self._validate_length(k):
            return set()
        
        unique_substrings = set()
        for i in range(len(self.target_string) - k + 1):
            substring = self.target_string[i:i+k]
            unique_substrings.add(substring)
        return unique_substrings

if __name__ == '__main__':
    extractor = SubstringExtractor("banana")
    target_length = 2
    result = extractor.extract_unique_substrings(target_length)
    print(result)