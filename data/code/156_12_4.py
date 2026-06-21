class NumericList:
    def __init__(self, data):
        if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("Input must be a list of numbers")
        self._data = data

    def calculate_average(self):
        if len(self._data) == 0:
            return 0
        total = sum(self._data)
        count = len(self._data)
        average = total / count
        return average

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    numeric_list = NumericList(sample_list)
    print(numeric_list.calculate_average())