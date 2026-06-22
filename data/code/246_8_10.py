class SumCalculator:
    @staticmethod
    def calculate_sum(a=10, b=5):
        return a + b

if __name__ == '__main__':
    result = SumCalculator.calculate_sum()
    print(result)