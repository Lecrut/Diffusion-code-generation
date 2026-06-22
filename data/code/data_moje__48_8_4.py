class LargestDataPointFinder:
    def __init__(self):
        self.data = [1.5, 3.2, 7.8, 2.1, 9.4, 4.6, 5.3]

    def get_largest(self):
        return max(self.data)

if __name__ == '__main__':
    finder = LargestDataPointFinder()
    print(finder.get_largest())