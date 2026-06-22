class SumCalculator:
    @staticmethod
    def sum(a, b):
        return a + b

if __name__ == '__main__':
    sample_a = 7
    sample_b = 9
    result = SumCalculator.sum(sample_a, sample_b)
    print(result)