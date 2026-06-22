class MinMaxFinder:
    def __init__(self):
        self.min_value = float('inf')
        self.max_value = float('-inf')

    def update_min_max(self, value):
        if value < self.min_value:
            self.min_value = value
        if value > self.max_value:
            self.max_value = value

def find_min_max(data):
    finder = MinMaxFinder()
    for value in data:
        finder.update_min_max(value)
    return finder.min_value, finder.max_value

if __name__ == '__main__':
    sample_data = [3, 1, 4, 1, 5, 9, 2, 6]
    minimum, maximum = find_min_max(sample_data)
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")