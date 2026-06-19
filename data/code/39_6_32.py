class SubstringFinder:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def find_pattern_indices(text, pattern):
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
    sample_text = "hello world hello"
    sample_pattern = "hello"
    finder = SubstringFinder(sample_text)
    result = SubstringFinder.find_pattern_indices(sample_text, sample_pattern)
    print(result)

    another_text = "banana banana"
    another_pattern = "na"
    another_result = SubstringFinder.find_pattern_indices(another_text, another_pattern)
    print(another_result)