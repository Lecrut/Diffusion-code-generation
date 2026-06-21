class NumberFinder:
    def __init__(self, data):
        self.data = data

    def find_smallest(self):
        if not self.data:
            raise ValueError("Input list cannot be empty")
        return min(self.data)

if __name__ == '__main__':
    finder = NumberFinder([42, 15, 89, 3, 77, 21])
    result = finder.find_smallest()
    print(result)