class MinMaxFinder:
    def __init__(self):
        self.min_value = None
        self.max_value = None

    def update(self, value):
        if self.min_value is None or value < self.min_value:
            self.min_value = value
        if self.max_value is None or value > self.max_value:
            self.max_value = value

def find_extremes(data):
    finder = MinMaxFinder()
    for value in data:
        finder.update(value)
    return (finder.min_value, finder.max_value) if finder.min_value is not None else (None, None)

if __name__ == '__main__':
    sample_list = [34, 12, 56, 89, 4, 72, 23]
    min_val, max_val = find_extremes(sample_list)
    print(f"Smallest value: {min_val}")
    print(f"Largest value: {max_val}")