class PrecisionCalculator:
    @staticmethod
    def add_two_numbers(a: float, b: float) -> float:
        return a + b

if __name__ == '__main__':
    num1 = 5.0
    num2 = 10.0
    result = PrecisionCalculator.add_two_numbers(num1, num2)
    print(result)