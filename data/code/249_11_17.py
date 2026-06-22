class LargestFinder:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.largest = max(data)

    def get_largest(self):
        return self.largest

if __name__ == '__main__':
    finder1 = LargestFinder([1, 5, 2, 8, 3])
    finder2 = LargestFinder([-10, -5, -20, -1])
    finder3 = LargestFinder([42])

    print(f"Largest in {finder1.get_largest()}: {finder1.get_largest()}")
    print(f"Largest in {finder2.get_largest()}: {finder2.get_largest()}")
    print(f"Largest in {finder3.get_largest()}: {finder3.get_largest()}")