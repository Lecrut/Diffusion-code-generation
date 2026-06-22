class SumCalculator:
    @staticmethod
    def add_numbers(a=5, b=3):
        return a + b

if __name__ == '__main__':
    result = SumCalculator.add_numbers()
    print(result)