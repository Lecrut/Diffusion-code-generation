class NumericalSequence:
    def __init__(self, numbers):
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("All elements must be numbers")
        self.numbers = numbers

    def average(self):
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    sample_numbers = [1.5, 2.3, 3.7]
    sequence = NumericalSequence(sample_numbers)
    print("Average:", sequence.average())