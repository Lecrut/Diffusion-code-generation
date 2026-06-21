class AverageCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, value):
        self.total += value
        self.count += 1

    def get_average(self):
        if self.count == 0:
            return 0
        return self.total / self.count

if __name__ == '__main__':
    calculator = AverageCalculator()
    sample_list = [10, 20, 30, 40, 50]
    for value in sample_list:
        calculator.add(value)
    print(calculator.get_average())

    calculator = AverageCalculator()
    sample_list_empty = []
    for value in sample_list_empty:
        calculator.add(value)
    print(calculator.get_average())

    calculator = AverageCalculator()
    sample_list_floats = [1.5, 2.5, 3.0]
    for value in sample_list_floats:
        calculator.add(value)
    print(calculator.get_average())