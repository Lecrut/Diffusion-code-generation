class LengthAnalyzer:
    @staticmethod
    def calculate_ratio(length1, length2):
        min_length = min(length1, length2)
        max_length = max(length1, length2)
        ratio = max_length / min_length
        return ratio

if __name__ == '__main__':
    a = 7
    b = 28
    ratio = LengthAnalyzer.calculate_ratio(a, b)
    print(ratio)