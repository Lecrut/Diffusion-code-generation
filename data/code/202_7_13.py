class RangeLargestFinder:
    def __init__(self, start=10, end=50):
        self.start = start
        self.end = end

    def find_largest(self):
        largest = self.start
        for num in range(self.start + 1, self.end + 1):
            if num > largest:
                largest = num
        return largest

if __name__ == '__main__':
    finder1 = RangeLargestFinder()
    print(f"Range: {finder1.start} to {finder1.end}, Largest: {finder1.find_largest()}")

    finder2 = RangeLargestFinder(start=100, end=150)
    print(f"Range: {finder2.start} to {finder2.end}, Largest: {finder2.find_largest()}")