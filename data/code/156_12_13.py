class NumericListProcessor:
    def __init__(self, data):
        self._data = data

    def calculate_average(self):
        if not self._data:
            return 0
        total = sum(self._data)
        count = len(self._data)
        average = total / count
        return average

if __name__ == '__main__':
    sample_data = [12, 24, 36, 48, 60]
    processor = NumericListProcessor(sample_data)
    avg = processor.calculate_average()
    print(avg)