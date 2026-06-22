class SequenceCalculator:
    def calculate_sum(self, numbers):
        total = 0
        for number in numbers:
            total += number
        return total

if __name__ == '__main__':
    calculator = SequenceCalculator()
    sample_sequence = [10, 20, 30, 40]
    result = calculator.calculate_sum(sample_sequence)
    print(f"The sum of {sample_sequence} is: {result}")