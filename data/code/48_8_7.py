class DataProcessor:
    def __init__(self):
        self.data = [3.5, 7.2, 1.8, 9.9, 4.1, 6.3]

    def get_largest_data_point(self):
        if not self.data:
            raise ValueError("Data list is empty")
        largest = self.data[0]
        for value in self.data[1:]:
            if value > largest:
                largest = value
        return largest

if __name__ == '__main__':
    processor = DataProcessor()
    result = processor.get_largest_data_point()
    print(result)