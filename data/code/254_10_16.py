class MinimumFinder:
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
    sample_list = [3, 1, 4, 1, 5, 9, 2, 8, 7, 6]
    finder = MinimumFinder(sample_list)
    try:
        result = finder.find_minimum()
        print(result)
    except ValueError as e:
        print(f"Error: {e}")