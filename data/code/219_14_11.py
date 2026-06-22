class MaxFinder:
    def __init__(self):
        self.max_value = None

    def update_max(self, number):
        if self.max_value is None or number > self.max_value:
            self.max_value = number

    def get_max(self):
        return self.max_value

if __name__ == '__main__':
    finder = MaxFinder()
    data = [15, 8, 42, 3, 99, 27, 50]
    for num in data:
        finder.update_max(num)
    result = finder.get_max()
    print(result)