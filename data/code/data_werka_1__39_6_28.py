class SubstringFinder:
    @staticmethod
    def find_all_occurrences(text, pattern):
        occurrences = []
        n = len(text)
        m = len(pattern)
        if m == 0:
            return occurrences
        for i in range(n - m + 1):
            if text[i:i+m] == pattern:
                occurrences.append((i, i + m))
        return occurrences

if __name__ == '__main__':
    text_sample = "hello world, hello universe"
    pattern_sample = "hello"
    result = SubstringFinder.find_all_occurrences(text_sample, pattern_sample)
    print(result)