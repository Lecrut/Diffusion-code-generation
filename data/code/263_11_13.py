class MinMaxFinder:
    def __init__(self):
        self.min_val = float('inf')
        self.max_val = float('-inf')

    def update(self, value):
        if value < self.min_val:
            self.min_val = value
        if value > self.max_val:
            self.max_val = value

def find_min_max(numbers):
    finder = MinMaxFinder()
    for number in numbers:
        finder.update(number)
    return (finder.min_val, finder.max_val)

if __name__ == '__main__':
    sample_list = [34, 78, 12, 90, 56]
    print(find_min_max(sample_list))