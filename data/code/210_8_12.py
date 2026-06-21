def calculate_range(data):
    if not data:
        return 0
    sorted_data = sorted(data)
    return sorted_data[-1] - sorted_data[0]

class RangeCalculator:
    def __init__(self, data):
        self.data = data

    def compute_range(self):
        if not self.data:
            return 0
        sorted_data = sorted(self.data)
        return sorted_data[-1] - sorted_data[0]

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    calculator = RangeCalculator(sample_data)
    print("Range of the dataset:", calculator.compute_range())