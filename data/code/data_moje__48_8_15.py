class DataPointFinder:
    def __init__(self):
        self.data_points = [3.5, 7.2, 1.9, 9.8, 4.1]

    def get_largest_data_point(self):
        if not self.data_points:
            return None
        largest = self.data_points[0]
        for value in self.data_points[1:]:
            if value > largest:
                largest = value
        return largest

if __name__ == "__main__":
    finder = DataPointFinder()
    result = finder.get_largest_data_point()
    print(result)