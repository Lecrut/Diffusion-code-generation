class SumCalculator:
    def __init__(self):
        self.total = 0

    def add_numbers(self, numbers):
        try:
            for number in numbers:
                self.total += int(number)
        except ValueError:
            raise ValueError("Error: Invalid input detected.")

    def get_total(self):
        return self.total

if __name__ == '__main__':
    calculator = SumCalculator()
    sample_numbers = ('10', '20', '30', '40', '50')
    try:
        calculator.add_numbers(sample_numbers)
        result = calculator.get_total()
        print(result)
    except ValueError as e:
        print(e)