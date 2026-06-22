class SubstringExtractor:
    def __init__(self, S):
        self.S = S

    def extract_substrings(self, L):
        n = len(self.S)
        if L <= 0 or L > n:
            return []
        substrings = []
        for i in range(n - L + 1):
            substrings.append(self.S[i:i+L])
        return substrings

if __name__ == '__main__':
    sample_string = "abcdefghijk"
    substring_length = 3
    extractor = SubstringExtractor(sample_string)
    result = extractor.extract_substrings(substring_length)
    print(result)