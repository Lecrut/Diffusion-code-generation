class LargestFinder:
    def __init__(self, data):
        if not data:
            raise ValueError("Data list cannot be empty")
        self.data = data

    def find_largest(self):
        largest = self.data[0]
        for element in self.data[1:]:
            if element > largest:
                largest = element
        return largest

if __name__ == '__main__':
    sample_list = [15, 8, 42, 3, 99, 27]
    finder = LargestFinder(sample_list)
    result = finder.find_largest()
    print(result)