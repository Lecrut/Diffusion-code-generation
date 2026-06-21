class RangeFinder:
    def __init__(self, data):
        self.data = data

    def find_range(self):
        if not self.data:
            return None
        minimum = min(self.data)
        maximum = max(self.data)
        return (minimum, maximum)

if __name__ == '__main__':
    finder1 = RangeFinder([1, 5, 2, 8, 3])
    finder2 = RangeFinder([])
    finder3 = RangeFinder([10])
    finder4 = RangeFinder([-5, 0, 5])

    print(f"Range of {finder1.data}: {finder1.find_range()}")
    print(f"Range of {finder2.data}: {finder2.find_range()}")
    print(f"Range of {finder3.data}: {finder3.find_range()}")
    print(f"Range of {finder4.data}: {finder4.find_range()}")