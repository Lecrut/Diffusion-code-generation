class MinFinder:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.data = data
        self.minimum = data[0]

    def find_min(self):
        for element in self.data[1:]:
            if element < self.minimum:
                self.minimum = element
        return self.minimum

if __name__ == '__main__':
    min_finder = MinFinder([3.14159, -0.5, 100.0, -99.999, 2.71828, -1.0])
    try:
        min_value = min_finder.find_min()
        print(min_value)
    except ValueError as e:
        print(f"Error: {e}")