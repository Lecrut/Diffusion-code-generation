import random

class MinFinder:
    def __init__(self):
        self.data = []

    def generate_data(self, size):
        self.data = [random.randint(-1000, 1000) for _ in range(size)]

    def find_minimum(self):
        if not self.data:
            raise ValueError("Input list cannot be empty")
        minimum = self.data[0]
        for item in self.data[1:]:
            if item < minimum:
                minimum = item
        return minimum

if __name__ == '__main__':
    finder = MinFinder()
    finder.generate_data(10)
    print(f"Generated data: {finder.data}")
    try:
        min_value = finder.find_minimum()
        print(f"Minimum value: {min_value}")
    except ValueError as e:
        print(e)