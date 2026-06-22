class SumCalculator:
    @staticmethod
    def add(a, b):
        return a + b

if __name__ == '__main__':
    value1 = 10
    value2 = 5
    result = SumCalculator.add(value1, value2)
    print(result)