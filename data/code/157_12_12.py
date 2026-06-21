class MinFinder:
    def __init__(self, data):
        self.data = data

    def find_min(self):
        return min(self.data)

if __name__ == '__main__':
    sample_list = [3.14, -1.5, 2.718, -10.0, 0.5, 42.0]
    finder = MinFinder(sample_list)
    result = finder.find_min()
    print(result)