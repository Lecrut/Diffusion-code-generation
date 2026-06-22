class SumCalculator:
    def __init__(self):
        self.total = 0.0

    def add(self, number):
        self.total += number

    def get_total(self):
        return self.total

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    for number in sample_numbers:
        calculator.add(number)
    print(calculator.get_total())