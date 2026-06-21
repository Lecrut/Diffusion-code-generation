class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    def calculate_mean(self):
        total = sum(self.data)
        count = len(self.data)
        return total / count if count > 0 else None

if __name__ == '__main__':
    processor = DataProcessor([15, 25, 35, 45])
    print(processor.calculate_mean())