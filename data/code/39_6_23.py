class SubstringFinder:

    def __init__(self, text):
        self.text = text

    def find_all_occurrences(self, pattern):
        occurrences = []
        n = len(self.text)
        m = len(pattern)
        if m == 0:
            return occurrences
        for i in range(n - m + 1):
            if self.text[i:i + m] == pattern:
                occurrences.append((i, i + m))
        return occurrences
if __name__ == '__main__':
    text_sample = 'abababa'
    finder = SubstringFinder(text_sample)
    pattern_sample_1 = 'aba'
    result_1 = finder.find_all_occurrences(pattern_sample_1)
    print(result_1)
    text_sample_2 = 'aaaaa'
    finder_2 = SubstringFinder(text_sample_2)
    pattern_sample_2 = 'aa'
    result_2 = finder_2.find_all_occurrences(pattern_sample_2)
    print(result_2)