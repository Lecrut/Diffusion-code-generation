class LengthAnalyzer:
    @staticmethod
    def analyze(length1, length2):
        return {
            'length1': length1,
            'length2': length2,
            'difference': abs(length1 - length2),
            'ratio': max(length1, length2) / min(length1, length2)
        }

if __name__ == '__main__':
    sample_length1 = 20
    sample_length2 = 40
    result = LengthAnalyzer.analyze(sample_length1, sample_length2)
    print(result)