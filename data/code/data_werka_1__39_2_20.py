class SubstringExtractor:
    def __init__(self, target_string):
        self.target_string = target_string

    def find_unique_substrings(self, k):
        unique_substrings = set()
        n = len(self.target_string)
        for i in range(n - k + 1):
            substring = self.target_string[i:i+k]
            unique_substrings.add(substring)
        return list(unique_substrings)

if __name__ == '__main__':
    extractor = SubstringExtractor("abacabad")
    k = 3
    print(extractor.find_unique_substrings(k))