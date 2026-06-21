class MinFinder:
    def __init__(self):
        self.min_value = None

    def find_minimum(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.min_value = data[0]
        for element in data[1:]:
            if element < self.min_value:
                self.min_value = element
        return self.min_value

if __name__ == '__main__':
    finder = MinFinder()
    large_list = [3.14159, -0.5, 100.0, -99.999, 2.71828, -1.0]
    min_value = finder.find_minimum(large_list)
    print(min_value)