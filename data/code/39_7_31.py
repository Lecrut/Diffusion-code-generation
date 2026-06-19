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
    S_sample = "abcdefghijk"
    L_sample1 = 3
    L_sample2 = 4
    
    extractor = SubstringExtractor(S_sample)
    
    result1 = extractor.extract_substrings(L_sample1)
    print(result1)
    
    result2 = extractor.extract_substrings(L_sample2)
    print(result2)