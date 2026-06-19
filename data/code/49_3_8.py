class LengthAnalyzer:
    @staticmethod
    def analyze_lengths(len1, len2):
        minimum = min(len1, len2)
        maximum = max(len1, len2)
        difference = abs(len1 - len2)
        return (minimum, maximum, difference)

if __name__ == '__main__':
    length1 = 30.5
    length2 = 45.8
    result = LengthAnalyzer.analyze_lengths(length1, length2)
    print(result)