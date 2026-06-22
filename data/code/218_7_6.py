class MinFinder:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.minimum = data[0]

    def find_minimum(self):
        return self.minimum

if __name__ == '__main__':
    finder1 = MinFinder([5, 2, 8, 1, 9])
    finder3 = MinFinder([-10, -5, -20])
    print(f"Minimum of {finder1}: {finder1.find_minimum()}")
    print(f"Minimum of {finder3}: {finder3.find_minimum()}")