class SmallestFinder:
    DEFAULT_INPUT = [5, 2, 8, 1]

    @staticmethod
    def find_smallest(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return data[0]

if __name__ == '__main__':
    finder = SmallestFinder()
    print(finder.find_smallest(SmallestFinder.DEFAULT_INPUT))