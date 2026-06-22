class LengthAnalyzer:
    @staticmethod
    def calculate_ratio(len1, len2):
        min_length = min(len1, len2)
        max_length = max(len1, len2)
        ratio = max_length / min_length
        return ratio

if __name__ == '__main__':
    length_a = 7
    length_b = 28
    analyzer = LengthAnalyzer()
    ratio = analyzer.calculate_ratio(length_a, length_b)
    print(ratio)