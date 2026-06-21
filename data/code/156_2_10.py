class ListAverageCalculator:
    def __init__(self, data):
        self._data = data

    def calculate_average(self):
        if not self._data:
            return 0
        return sum(self._data) / len(self._data)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    calculator = ListAverageCalculator(sample_list)
    average = calculator.calculate_average()
    print(average)