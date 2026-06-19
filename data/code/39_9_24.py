class SubstringFinder:
    def __init__(self, phrase):
        self.phrase = phrase

    def find_all_substrings(self):
        n = len(self.phrase)
        substrings = set()
        for i in range(n):
            for j in range(i + 1, n + 1):
                substrings.add(self.phrase[i:j])
        return sorted(list(substrings))

if __name__ == '__main__':
    sample_phrase_1 = "abcabc"
    finder_1 = SubstringFinder(sample_phrase_1)
    print(finder_1.find_all_substrings())

    sample_phrase_2 = "banana"
    finder_2 = SubstringFinder(sample_phrase_2)
    print(finder_2.find_all_substrings())

    sample_phrase_3 = "aaaa"
    finder_3 = SubstringFinder(sample_phrase_3)
    print(finder_3.find_all_substrings())