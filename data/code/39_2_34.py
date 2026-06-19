class SubstringExtractor:
    def __init__(self):
        self.target_string = ""
    
    def set_target(self, s: str):
        self.target_string = s
    
    def extract_unique_substrings(self, k: int) -> set:
        if k <= 0 or k > len(self.target_string):
            return set()
        substrings = set()
        for i in range(len(self.target_string) - k + 1):
            substrings.add(self.target_string[i:i+k])
        return substrings

if __name__ == '__main__':
    extractor = SubstringExtractor()
    target_string = "banana"
    substring_length = 2
    extractor.set_target(target_string)
    result = extractor.extract_unique_substrings(substring_length)
    print(result)