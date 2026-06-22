class MiddleValueFinder:
    def __init__(self, data):
        self.data = data

    def find_middle_value(self):
        n = len(self.data)
        if n == 0:
            return None
        sorted_data = sorted(self.data)
        middle_index = n // 2
        return sorted_data[middle_index]

if __name__ == '__main__':
    finder = MiddleValueFinder([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print("Middle value:", finder.find_middle_value())
    odd_finder = MiddleValueFinder([1, 2, 3, 4, 5])
    print("Middle value for odd length list:", odd_finder.find_middle_value())
    large_finder = MiddleValueFinder(list(range(1000000)))
    print("Middle value for large list:", large_finder.find_middle_value())