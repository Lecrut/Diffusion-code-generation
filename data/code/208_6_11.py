class DataProcessor:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        if not self.data:
            return 0
        total = sum(self.data)
        count = len(self.data)
        return total / count

if __name__ == '__main__':
    processor = DataProcessor([10, 20, 30, 40])
    print(processor.calculate_mean())