class LengthAnalyzer:
    @staticmethod
    def analyze_lengths(len1, len2):
        min_len = LengthAnalyzer._find_minimum(len1, len2)
        max_len = LengthAnalyzer._find_maximum(len1, len2)
        abs_diff = LengthAnalyzer._calculate_absolute_difference(len1, len2)
        return (min_len, max_len, abs_diff)

    @staticmethod
    def _find_minimum(a, b):
        return a if a < b else b

    @staticmethod
    def _find_maximum(a, b):
        return a if a > b else b

    @staticmethod
    def _calculate_absolute_difference(a, b):
        return abs(a - b)

if __name__ == '__main__':
    length1 = 45.3
    length2 = 60.7
    result = LengthAnalyzer.analyze_lengths(length1, length2)
    print(result)