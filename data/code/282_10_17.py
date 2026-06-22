class SequenceSumCalculator:
    def calculate_sum(self, numbers):
        return sum(numbers)

if __name__ == '__main__':
    calculator = SequenceSumCalculator()
    sample_numbers = [1, 2, 3, 4, 5]
    print(calculator.calculate_sum(sample_numbers))