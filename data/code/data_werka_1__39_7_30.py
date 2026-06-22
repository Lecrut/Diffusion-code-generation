class SubstringExtractor:
    def __init__(self, S):
        self.S = S

    def extract(self, L):
        n = len(self.S)
        if L <= 0 or L > n:
            raise ValueError("Length L must be greater than 0 and less than or equal to the length of the string.")
        substrings = []
        for i in range(n - L + 1):
            substrings.append(self.S[i:i+L])
        return substrings

if __name__ == '__main__':
    S_sample = "abcdefghijk"
    L_sample = 3
    extractor = SubstringExtractor(S_sample)
    result = extractor.extract(L_sample)
    print(result)