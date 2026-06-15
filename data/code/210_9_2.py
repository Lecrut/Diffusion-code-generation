class Statistics:
    def __init__(self):
        self._data = None
        self._range = None
    def set_data(self, data):
        if not isinstance(data, list) or not data:
            raise ValueError("Input must be a non-empty list of numbers.")
        self._data = data
        self.calculate_range()
    def calculate_range(self):
        if self._data is None:
            self._range = None
            return
        minimum = min(self._data)
        maximum = max(self._data)
        self._range = maximum - minimum
    def get_range(self):
        if self._range is None:
            raise AttributeError("Range has not been calculated. Set data first.")
        return self._range
if __name__ == '__main__':
    stats_calculator = Statistics()
    sample_data_1 = [10, 5, 20, 15, 8]
    print(f"Data set 1: {sample_data_1}")
    stats_calculator.set_data(sample_data_1)
    range_1 = stats_calculator.get_range()
    print(f"Range of data set 1: {range_1}")
    sample_data_2 = [3, 9, 1, 5, 7]
    print(f"\nData set 2: {sample_data_2}")
    stats_calculator.set_data(sample_data_2)
    range_2 = stats_calculator.get_range()
    print(f"Range of data set 2: {range_2}")
    try:
        stats_calculator.get_range()
    except AttributeError as e:
        print(f"\nCaught expected error: {e}")