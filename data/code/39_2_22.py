class SubstringExtractor:
    def __init__(self, string):
        self.string = string

    def extract_substrings(self, length):
        if length <= 0 or length > len(self.string):
            return set()
        
        unique_substrings = set()
        for start in range(len(self.string) - length + 1):
            substring = self.string[start:start+length]
            unique_substrings.add(substring)
        
        return unique_substrings

if __name__ == '__main__':
    sample_string = "banana"
    k = 2
    extractor = SubstringExtractor(sample_string)
    result = extractor.extract_substrings(k)
    print(result)