class SubstringExtractor:
    def __init__(self, target_string):
        self.target_string = target_string

    def extract_unique_substrings(self, k: int) -> set:
        if k <= 0 or k > len(self.target_string):
            return set()
        
        unique_substrings = set()
        n = len(self.target_string)
        
        for i in range(n - k + 1):
            substring = self.target_string[i:i+k]
            unique_substrings.add(substring)
        
        return unique_substrings

if __name__ == '__main__':
    target_string = "hello"
    k = 2
    extractor = SubstringExtractor(target_string)
    result = extractor.extract_unique_substrings(k)
    print(result)