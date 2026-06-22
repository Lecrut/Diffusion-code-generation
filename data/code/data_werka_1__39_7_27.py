class SubstringExtractor:

    def __init__(self, S):
        self.S = S

    def extract_substrings(self, L):
        n = len(self.S)
        if L <= 0 or L > n:
            return []
        substrings = []
        for i in range(n - L + 1):
            substrings.append(self.S[i:i + L])
        return substrings
if __name__ == '__main__':
    S_sample = 'abcdefghijk'
    L_sample = 3
    extractor = SubstringExtractor(S_sample)
    result = extractor.extract_substrings(L_sample)
    print(result)
    S_sample_2 = 'xyzabcde'
    L_sample_2 = 4
    extractor_2 = SubstringExtractor(S_sample_2)
    result_2 = extractor_2.extract_substrings(L_sample_2)
    print(result_2)