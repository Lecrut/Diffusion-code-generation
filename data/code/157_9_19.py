class NumberFinder:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.data = data

    def find_smallest_iterative(self):
        smallest = self.data[0]
        for element in self.data[1:]:
            if element < smallest:
                smallest = element
        return smallest

if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 56, 7]
    finder = NumberFinder(sample_list)
    result = finder.find_smallest_iterative()
    print(result)