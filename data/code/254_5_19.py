import random

class MinFinder:
    def __init__(self):
        self.min_value = None

    def find_minimum(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.min_value = data[0]
        for item in data[1:]:
            if item < self.min_value:
                self.min_value = item
        return self.min_value

if __name__ == '__main__':
    min_finder = MinFinder()
    sample_data = [random.randint(-100, 100) for _ in range(10)]
    print("Sample Data:", sample_data)
    minimum_value = min_finder.find_minimum(sample_data)
    print("Minimum Value:", minimum_value)