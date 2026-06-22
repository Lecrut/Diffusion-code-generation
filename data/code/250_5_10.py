import numpy as np

class DataProcessor:
    def __init__(self):
        self.data = []

    @staticmethod
    def validate_data(data):
        if not data:
            raise ValueError("Data cannot be empty")
        return np.array(data)

    def add_data(self, value):
        self.data.extend(self.validate_data([value]))

    def calculate_average(self):
        if not self.data.size:
            return 0.0
        return np.mean(self.data)

if __name__ == '__main__':
    processor = DataProcessor()
    processor.add_data(10)
    processor.add_data(20)
    processor.add_data(30)
    print(processor.calculate_average())