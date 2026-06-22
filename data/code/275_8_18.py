class MaxMinFinder:
    def __init__(self):
        self.max_val = None
        self.min_val = None

    def update(self, num):
        if self.max_val is None or num > self.max_val:
            self.max_val = num
        if self.min_val is None or num < self.min_val:
            self.min_val = num

def find_max_min(numbers):
    finder = MaxMinFinder()
    for num in numbers:
        finder.update(num)
    return finder.max_val, finder.min_val

if __name__ == '__main__':
    sample_numbers = [3, 5, 1, 8, -2, 7]
    max_value, min_value = find_max_min(sample_numbers)
    print(f"Max: {max_value}, Min: {min_value}")