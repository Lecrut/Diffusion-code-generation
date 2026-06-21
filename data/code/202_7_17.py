class RangeFinder:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def find_largest(self):
        return max(self.start, self.end)

if __name__ == '__main__':
    finder1 = RangeFinder(5, 10)
    print(f"Range: {finder1.start}-{finder1.end}, Largest: {finder1.find_largest()}")

    finder2 = RangeFinder(-10, -5)
    print(f"Range: {finder2.start}-{finder2.end}, Largest: {finder2.find_largest()}")

    finder3 = RangeFinder(0, 0)
    print(f"Range: {finder3.start}-{finder3.end}, Largest: {finder3.find_largest()}")

    finder4 = RangeFinder(-50, 100)
    print(f"Range: {finder4.start}-{finder4.end}, Largest: {finder4.find_largest()}")