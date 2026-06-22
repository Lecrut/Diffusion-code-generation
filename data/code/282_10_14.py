class SequenceCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_sum(self):
        return sum([num for num in self.numbers])

if __name__ == '__main__':
    calculator = SequenceCalculator([1, 5, 10, 15, 20])
    result = calculator.calculate_sum()
    print(result)