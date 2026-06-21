class LargestFinder:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.data = data
        self.largest = self._find_largest()

    def _find_largest(self):
        largest = self.data[0]
        for x in self.data[1:]:
            if x > largest:
                largest = x
        return largest

if __name__ == '__main__':
    finder1 = LargestFinder([3, 1, 4, 1, 5, 9, 2])
    print(f"The largest in {finder1.data} is: {finder1.largest}")
    finder2 = LargestFinder([-10, -5, -20, -1])
    print(f"The largest in {finder2.data} is: {finder2.largest}")
    finder3 = LargestFinder([42])
    print(f"The largest in {finder3.data} is: {finder3.largest}")
    finder4 = LargestFinder([100, 50, 200, 10])
    print(f"The largest in {finder4.data} is: {finder4.largest}")