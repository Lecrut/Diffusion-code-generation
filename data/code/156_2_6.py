class AverageCalculator:
    def __init__(self, data):
        self._data = data

    def calculate(self):
        if not self._data:
            return 0
        return sum(self._data) / len(self._data)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    calculator = AverageCalculator(sample_data)
    average = calculator.calculate()
    print(average)