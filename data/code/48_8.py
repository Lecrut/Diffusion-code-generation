class DataProcessor:
    def __init__(self):
        self.data = [1.5, 2.3, 4.7, 3.1, 9.2, 5.6]

    def get_largest_value(self):
        return max(self.data)

if __name__ == '__main__':
    processor = DataProcessor()
    result = processor.get_largest_value()
    print(result)