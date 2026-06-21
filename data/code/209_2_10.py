import numpy as np

class DataProcessor:
    def __init__(self, data):
        self.data = data
    
    def calculate_mean(self):
        return np.mean(self.data)

if __name__ == '__main__':
    processor = DataProcessor([100, 200, 300])
    average = processor.calculate_mean()
    print(average)