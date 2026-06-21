class NumericListProcessor:
    def __init__(self, data):
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("All elements must be numbers")
        self._data = data

    def calculate_average(self):
        if not self._data:
            return 0
        total = sum(self._data)
        count = len(self._data)
        average = total / count
        return average

if __name__ == '__main__':
    sample_numbers = [12, 24, 36, 48, 60]
    processor = NumericListProcessor(sample_numbers)
    avg = processor.calculate_average()
    print(avg)