class DataProcessor:
    def __init__(self):
        self.data = [1.5, 2.3, 4.1, 3.9, 5.0, 0.5, 6.2, 7.8, 8.1, 9.0]

    def get_largest_data_point(self):
        return max(self.data)

if __name__ == '__main__':
    processor = DataProcessor()
    result = processor.get_largest_data_point()
    print(result)