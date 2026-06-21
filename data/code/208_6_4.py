class DataProcessor:
    def __init__(self, data):
        self.data = data

    def calculate_mean(self):
        if not self.data:
            return None
        total = sum(self.data)
        count = len(self.data)
        return total / count

if __name__ == '__main__':
    processor = DataProcessor([10, 20, 30, 40])
    print("Mean:", processor.calculate_mean())
    
    processor = DataProcessor([])
    print("Mean of empty list:", processor.calculate_mean())