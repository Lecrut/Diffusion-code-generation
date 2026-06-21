class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count

if __name__ == '__main__':
    sample_numbers = [5, 10, 15, 20, 25]
    calculator = AverageCalculator(sample_numbers)
    avg = calculator.calculate_average()
    print(avg)