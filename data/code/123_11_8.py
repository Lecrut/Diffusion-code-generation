class CumulativeSumCalculator:
    SAMPLE_VALUES = [1, 5, 10, 2, 8]

    @staticmethod
    def calculate_total_sum(numbers):
        total = 0
        for number in numbers:
            total += number
        return total

if __name__ == '__main__':
    calculator = CumulativeSumCalculator()
    result = calculator.calculate_total_sum(CumulativeSumCalculator.SAMPLE_VALUES)
    print(result)