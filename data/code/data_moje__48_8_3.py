class DataProcessor:
    def __init__(self):
        self.data = [3.14, 2.71, 1.62, 0.58, 4.0, -2.5]

    def get_largest(self):
        return max(self.data)

if __name__ == '__main__':
    processor = DataProcessor()
    print(processor.get_largest())