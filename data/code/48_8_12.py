class MaxFinder:
    def __init__(self):
        self.data_points = [3.14, 2.71, 1.41, 9.81, 0.57, 4.5]

    def get_largest_point(self):
        if not self.data_points:
            return None
        return max(self.data_points)

if __name__ == '__main__':
    finder = MaxFinder()
    print(finder.get_largest_point())