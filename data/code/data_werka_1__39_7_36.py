class SubstringExtractor:
    def __init__(self, S):
        self.S = S

    @staticmethod
    def validate_length(L, n):
        return 0 < L <= n

    def extract_substrings(self, L):
        n = len(self.S)
        if not self.validate_length(L, n):
            return []
        substrings = []
        for i in range(n - L + 1):
            substrings.append(self.S[i:i+L])
        return substrings

if __name__ == '__main__':
    S_sample = "abcdefghijk"
    L_sample = 3
    extractor = SubstringExtractor(S_sample)
    result = extractor.extract_substrings(L_sample)
    print(result)