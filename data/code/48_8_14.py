class DataProcessor:
    def __init__(self):
        self.data = [3.5, 7.2, 4.1, 9.8, 2.3, 5.6, 8.9]

    def get_largest(self):
        if not self.data:
            return None
        largest_value = self.data[0]
        for value in self.data[1:]:
            if value > largest_value:
                largest_value = value
        return largest_value

if __name__ == '__main__':
    processor = DataProcessor()
    result = processor.get_largest()
    print(result)