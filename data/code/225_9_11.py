class MinMaxFinder:
    def __init__(self):
        self.min_val = None
        self.max_val = None

    def update_min_max(self, value):
        if self.min_val is None or value < self.min_val:
            self.min_val = value
        if self.max_val is None or value > self.max_val:
            self.max_val = value

def find_min_max_stream(data_stream):
    finder = MinMaxFinder()
    for number in data_stream:
        finder.update_min_max(number)
    return finder.min_val, finder.max_val

if __name__ == '__main__':
    sample_data = [10, 5, 20, -3, 15, 8, 25, -10]
    min_result, max_result = find_min_max_stream(sample_data)
    print(f"Minimum value: {min_result}")
    print(f"Maximum value: {max_result}")

    sample_data_large = [1000, -500, 999, 0, 5000, -100]
    min_result_large, max_result_large = find_min_max_stream(sample_data_large)
    print(f"Minimum value (large): {min_result_large}")
    print(f"Maximum value (large): {max_result_large}")