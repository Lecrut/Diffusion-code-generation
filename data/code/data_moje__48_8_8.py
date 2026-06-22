class DataProcessor:
    def __init__(self):
        self.data_points = [3.14, 2.71, 1.41, 1.73, 0.577]

    def get_largest_data_point(self):
        largest = self.data_points[0]
        for value in self.data_points[1:]:
            if value > largest:
                largest = value
        return largest

if __name__ == '__main__':
    processor = DataProcessor()
    print(processor.get_largest_data_point())