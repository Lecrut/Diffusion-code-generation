class DataProcessor:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        if len(self.data) == 0:
            return None
        total = sum(self.data)
        count = len(self.data)
        return total / count

if __name__ == '__main__':
    processor1 = DataProcessor([10, 20, 30, 40])
    print(processor1.calculate_mean())

    processor2 = DataProcessor([-5, 0, 5])
    print(processor2.calculate_mean())

    processor3 = DataProcessor([])
    print(processor3.calculate_mean())