class MinFinder:
    def __init__(self, data):
        self.data = data

    def find_min(self):
        return min(self.data)

if __name__ == '__main__':
    sample_data = [15, 3, 8, 22, 1]
    finder = MinFinder(sample_data)
    smallest = finder.find_min()
    print(smallest)