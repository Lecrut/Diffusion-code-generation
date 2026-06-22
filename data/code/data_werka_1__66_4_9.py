class IncreasingPairsValidator:
    def __init__(self, numbers):
        if not all(isinstance(x, float) for x in numbers):
            raise ValueError("All elements must be floating-point numbers.")
        self.numbers = numbers

    def validate_pairs(self):
        return [self.numbers[i] < self.numbers[i + 1] for i in range(len(self.numbers) - 1)]

if __name__ == '__main__':
    sample_values = [3.0, 4.5, 6.2, 7.8, 9.1]
    validator = IncreasingPairsValidator(sample_values)
    result = validator.validate_pairs()
    print(result)