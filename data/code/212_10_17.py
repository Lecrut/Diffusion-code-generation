class MinMaxFinder:
    def __init__(self):
        self.min_value = float('inf')
        self.max_value = float('-inf')

    def update_values(self, number):
        if number < self.min_value:
            self.min_value = number
        if number > self.max_value:
            self.max_value = number

    def get_min_max(self):
        return self.min_value, self.max_value

if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_list = [10, 5, 20, 8, 15]
    for num in sample_list:
        finder.update_values(num)
    min_val, max_val = finder.get_min_max()
    print(f"Minimum: {min_val}")
    print(f"Maximum: {max_val}")