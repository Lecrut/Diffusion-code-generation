class MinFinder:
    def __init__(self, data):
        self.data = data

    def find_min(self):
        return min(self.data)

if __name__ == '__main__':
    sample_data = [42, 15, 89, 3, 77, 21]
    finder = MinFinder(sample_data)
    print(finder.find_min())