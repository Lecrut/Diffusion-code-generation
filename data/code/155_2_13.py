class FloatSumCalculator:
    @staticmethod
    def sum_floats(numbers):
        total = 0.0
        for number in numbers:
            total += number
        return total

if __name__ == '__main__':
    sample_values = [1.23456789, 2.34567890, 3.45678901]
    calculator = FloatSumCalculator()
    result = calculator.sum_floats(sample_values)
    print(result)