class SumCalculator:
    @staticmethod
    def calculate_sum(a=10, b=25, c=40):
        return a + b + c

if __name__ == '__main__':
    result = SumCalculator.calculate_sum()
    print(result)