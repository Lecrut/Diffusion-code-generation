class Statistics:
    def __init__(self):
        self._data = []
        self._range = None
    def add_data(self, data):
        self._data.extend(data)
    def calculate_range(self):
        if not self._data:
            self._range = None
            return None
        minimum = min(self._data)
        maximum = max(self._data)
        self._range = maximum - minimum
        return self._range
if __name__ == '__main__':
    stats_calculator = Statistics()
    sample_dataset_1 = [10, 5, 20, 15, 8]
    sample_dataset_2 = [3, 1, 9, 4, 7]
    sample_empty_dataset = []
    stats_calculator.add_data(sample_dataset_1)
    range1 = stats_calculator.calculate_range()
    print(f"Range of dataset 1: {range1}")
    stats_calculator.add_data(sample_dataset_2)
    range2 = stats_calculator.calculate_range()
    print(f"Range of dataset 2: {range2}")
    stats_calculator.add_data(sample_empty_dataset)
    range3 = stats_calculator.calculate_range()
    print(f"Range of empty dataset: {range3}")