class MaxFinder:
    def __init__(self, numbers):
        if not numbers:
            raise ValueError("Input list cannot be empty")
        self.largest = max(numbers)

    def get_largest(self):
        return self.largest

if __name__ == '__main__':
    finder1 = MaxFinder([3.14, 1.618, 2.718, 0.577])
    finder2 = MaxFinder([-10.5, -5.2, -20.1, -1.0])
    finder3 = MaxFinder([1.0, 1.0, 1.0, 1.0])
    finder4 = MaxFinder([99.99999999999999, 100.0])

    print(f"Largest in {finder1.get_largest()}: {finder1.get_largest()}")
    print(f"Largest in {finder2.get_largest()}: {finder2.get_largest()}")
    print(f"Largest in {finder3.get_largest()}: {finder3.get_largest()}")
    print(f"Largest in {finder4.get_largest()}: {finder4.get_largest()}")