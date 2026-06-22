import random

class MinFinder:
    def __init__(self):
        self.minimum = None

    def update_minimum(self, value):
        if self.minimum is None or value < self.minimum:
            self.minimum = value

def find_minimum(data):
    finder = MinFinder()
    for item in data:
        finder.update_minimum(item)
    return finder.minimum

if __name__ == '__main__':
    sample_data = [random.randint(1, 100) for _ in range(10)]
    print("Sample Data:", sample_data)
    result = find_minimum(sample_data)
    print("Minimum Value:", result)