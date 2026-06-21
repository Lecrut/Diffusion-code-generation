class DataProcessor:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        total = sum(self.data)
        count = len(self.data)
        return total / count if count > 0 else None

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    processor = DataProcessor(sample_data)
    print(processor.calculate_mean())