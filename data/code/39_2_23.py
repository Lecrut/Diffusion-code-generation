class SubstringExtractor:
    def __init__(self, text):
        self.text = text

    def extract_unique_substrings(self, k):
        if k <= 0 or k > len(self.text):
            return set()
        
        unique_substrings = set()
        for i in range(len(self.text) - k + 1):
            substring = self.text[i:i+k]
            unique_substrings.add(substring)
        
        return unique_substrings

if __name__ == '__main__':
    extractor = SubstringExtractor("banana")
    k = 2
    result = extractor.extract_unique_substrings(k)
    print(result)