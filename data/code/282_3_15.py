class SumCalculator:
    def __init__(self):
        self.total = 0.0

    def add_number(self, number):
        self.total += number

    def get_total(self):
        return self.total

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_numbers = [1.1, 2.2, 3.3, 4.4, 5.5]
    for number in sample_numbers:
        calculator.add_number(number)
    print(calculator.get_total())