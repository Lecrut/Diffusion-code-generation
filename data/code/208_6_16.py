class DataProcessor:
    def __init__(self, data):
        if not all(isinstance(x, (int, float)) for x in data) or len(data) == 0:
            raise ValueError("Data must be a non-empty list of numbers")
        self.data = data

    def calculate_mean(self):
        total = sum(self.data)
        count = len(self.data)
        return total / count if count > 0 else None

if __name__ == '__main__':
    processor = DataProcessor([15, 25, 35, 45])
    print(processor.calculate_mean())