class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        if not self.numbers:
            return 0
        total = sum(self.numbers)
        count = len(self.numbers)
        average = total / count
        return average

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    calculator = AverageCalculator(sample_list)
    avg = calculator.calculate_average()
    print(avg)