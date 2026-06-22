class SumCalculator:
    MAX_SEQUENCE_LENGTH = 1000

    @staticmethod
    def sum_large_sequence(numbers):
        if len(numbers) > SumCalculator.MAX_SEQUENCE_LENGTH:
            raise ValueError("Sequence too long")
        return sum(numbers)

if __name__ == '__main__':
    sample_numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    calculator = SumCalculator()
    result = calculator.sum_large_sequence(sample_numbers)
    print(result)