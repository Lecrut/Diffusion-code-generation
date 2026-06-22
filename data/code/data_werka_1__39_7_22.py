class SubstringExtractor:
    def __init__(self, S):
        self.S = S

    def extract(self, L):
        n = len(self.S)
        if L <= 0 or L > n:
            raise ValueError("Invalid length for substring extraction")
        substrings = []
        for i in range(n - L + 1):
            substrings.append(self.S[i:i+L])
        return substrings

if __name__ == '__main__':
    S_sample = "abcdefghijk"
    L_sample = 3
    extractor = SubstringExtractor(S_sample)
    try:
        result = extractor.extract(L_sample)
        print(result)
    except ValueError as e:
        print(e)