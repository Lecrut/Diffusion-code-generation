class SubstringExtractor:
    def __init__(self, S, L):
        self.S = S
        self.L = L
        if L <= 0 or L > len(S):
            raise ValueError("Length L must be positive and less than or equal to the length of the string S.")

    def extract(self):
        substrings = []
        n = len(self.S)
        for i in range(n - self.L + 1):
            substrings.append(self.S[i:i+self.L])
        return substrings

if __name__ == '__main__':
    try:
        S_sample = "abcdefghijk"
        L_sample = 3
        extractor = SubstringExtractor(S_sample, L_sample)
        result = extractor.extract()
        print(result)
    except ValueError as e:
        print(e)