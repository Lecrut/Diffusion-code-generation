class MinMaxFinder:
    def __init__(self):
        self.minimum = None
        self.maximum = None

    def update(self, value):
        if self.minimum is None or value < self.minimum:
            self.minimum = value
        if self.maximum is None or value > self.maximum:
            self.maximum = value

def find_min_max(data):
    finder = MinMaxFinder()
    for value in data:
        finder.update(value)
    return finder.minimum, finder.maximum

if __name__ == '__main__':
    large_list = [3.1415926535, -0.5, 100.75, -99.999, 50.0]
    minimum_val, maximum_val = find_min_max(large_list)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")

    another_list = [1.0, 2.5, -3.2, 4.8, 0.9]
    minimum_val_2, maximum_val_2 = find_min_max(another_list)
    print(f"Minimum: {minimum_val_2}")
    print(f"Maximum: {maximum_val_2}")

    empty_list = []
    minimum_val_3, maximum_val_3 = find_min_max(empty_list)
    print(f"Empty list result (Min): {minimum_val_3}")