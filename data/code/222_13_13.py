class StringMinimizer:
    def __init__(self, data):
        self.data = data

    def find_minimum(self):
        if not self.data:
            raise ValueError("Input list cannot be empty")
        minimum = self.data[0]
        for item in self.data[1:]:
            if item < minimum:
                minimum = item
        return minimum

if __name__ == '__main__':
    minimizer = StringMinimizer(["apple", "banana", "cherry"])
    print(minimizer.find_minimum())