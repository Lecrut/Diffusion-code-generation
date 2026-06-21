class MeanCalculator:
    def __init__(self, numbers):
        if not isinstance(numbers, list) or len(numbers) == 0:
            raise ValueError("Input must be a non-empty list of floats")
        self.numbers = numbers

    def calculate_mean(self):
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.5, 4.5]
    calculator = MeanCalculator(sample_values)
    print("Mean:", calculator.calculate_mean())