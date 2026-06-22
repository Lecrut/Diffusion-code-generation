class MaxDataPointFinder:
    def __init__(self):
        self.data = [1.1, 5.5, 3.3, 9.9, 2.2, 7.7]

    def get_largest_value(self):
        max_val = self.data[0]
        for value in self.data:
            if value > max_val:
                max_val = value
        return max_val

if __name__ == '__main__':
    finder = MaxDataPointFinder()
    result = finder.get_largest_value()
    print(result)