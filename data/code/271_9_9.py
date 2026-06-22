class SubstringFinder:
    def __init__(self, text):
        self.text = text

    def find_unique_substrings(self):
        substrings = set()
        n = len(self.text)
        for i in range(n):
            for j in range(i + 3, n + 1):
                substrings.add(self.text[i:j])
        return sorted(substrings)

if __name__ == '__main__':
    sample_text = "abcde"
    finder = SubstringFinder(sample_text)
    unique_substrings = finder.find_unique_substrings()
    print(unique_substrings)