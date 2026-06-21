class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_range(self):
        if not self.data:
            return None
        minimum = min(self.data)
        maximum = max(self.data)
        return (minimum, maximum)

if __name__ == '__main__':
    analyzer1 = DataAnalyzer([1, 5, 2, 8, 3])
    analyzer2 = DataAnalyzer([])
    analyzer3 = DataAnalyzer([10])
    analyzer4 = DataAnalyzer([-5, 0, 5])

    print(f"Range of {analyzer1.data}: {analyzer1.find_range()}")
    print(f"Range of {analyzer2.data}: {analyzer2.find_range()}")
    print(f"Range of {analyzer3.data}: {analyzer3.find_range()}")
    print(f"Range of {analyzer4.data}: {analyzer4.find_range()}")