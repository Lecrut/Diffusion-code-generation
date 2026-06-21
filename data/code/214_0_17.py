class NumberFinder:
    def __init__(self, data):
        if not data:
            raise ValueError("Input list cannot be empty")
        self.data = data

    def find_smallest(self):
        return min(self.data)

if __name__ == '__main__':
    sample_list = [42, 15, 89, 3, 77, 21]
    finder = NumberFinder(sample_list)
    result = finder.find_smallest()
    print(result)