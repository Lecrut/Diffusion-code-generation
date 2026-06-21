class Statistics:
    def __init__(self):
        self._data = []
    
    def add_data(self, data):
        if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("Input must be a non-empty list of numbers.")
        self._data.extend(data)
    
    def calculate_range(self):
        if not self._data:
            return None
        minimum = min(self._data)
        maximum = max(self._data)
        return maximum - minimum

if __name__ == '__main__':
    stats_calculator = Statistics()
    sample_dataset_1 = [10, 5, 20, 15]
    sample_dataset_2 = [3, 8, 1, 9, 4]

    stats_calculator.add_data(sample_dataset_1)
    print("Range of sample_dataset_1:", stats_calculator.calculate_range())

    stats_calculator.add_data(sample_dataset_2)
    print("Range after adding sample_dataset_2:", stats_calculator.calculate_range())