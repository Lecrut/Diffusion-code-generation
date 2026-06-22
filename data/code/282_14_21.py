class SumCalculator:
    def __init__(self, input_string):
        self.input_string = input_string

    def parse_numbers(self):
        return [float(x.strip()) for x in self.input_string.split(',') if x.strip()]

    def calculate_total(self):
        numbers = self.parse_numbers()
        return sum(numbers)

if __name__ == '__main__':
    calculator = SumCalculator("10, 5.5, 20, 3.5")
    print(f"Input string: {calculator.input_string}")
    print(f"Calculated sum: {calculator.calculate_total()}")