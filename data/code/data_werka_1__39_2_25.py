class SubstringExtractor:
    def __init__(self, target_string):
        self.target_string = target_string

    def extract_unique_substrings(self, k: int) -> set:
        if k <= 0 or k > len(self.target_string):
            return set()
        
        unique_substrings = set()
        for i in range(len(self.target_string) - k + 1):
            substring = self.target_string[i:i+k]
            unique_substrings.add(substring)
        
        return unique_substrings

if __name__ == '__main__':
    SAMPLE_STRING = "banana"
    SUBSTRING_LENGTH = 2
    extractor = SubstringExtractor(SAMPLE_STRING)
    result = extractor.extract_unique_substrings(SUBSTRING_LENGTH)
    print(result)