class SumCalculator:
    @staticmethod
    def add(a, b):
        return a + b

if __name__ == '__main__':
    sample_num1 = 10
    sample_num2 = 15
    result = SumCalculator.add(sample_num1, sample_num2)
    print(result)