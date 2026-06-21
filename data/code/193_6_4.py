class MixedNumberSum:
    def __init__(self):
        self.total = 0

    def add_number(self, number):
        if isinstance(number, int):
            self.total += number
        elif isinstance(number, float):
            self.total += number

    def get_total(self):
        return self.total

if __name__ == '__main__':
    calculator = MixedNumberSum()
    sample_values = [1, 2.5, -3, 4.75]
    for value in sample_values:
        calculator.add_number(value)
    print(calculator.get_total())