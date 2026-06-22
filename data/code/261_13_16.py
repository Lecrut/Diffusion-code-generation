import random

class DataProcessor:
    def __init__(self):
        self.data = [random.randint(1, 1000) for _ in range(100)]
    
    def sort_data(self):
        return sorted(self.data)
    
    def calculate_median(self, data):
        n = len(data)
        mid = n // 2
        if n % 2 == 0:
            return (data[mid - 1] + data[mid]) / 2
        else:
            return data[mid]

if __name__ == '__main__':
    processor = DataProcessor()
    sorted_data = processor.sort_data()
    median_value = processor.calculate_median(sorted_data)
    print(median_value)