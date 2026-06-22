class MinFinder:
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    def find_min(self):
        try:
            min_val = next(self.iterable)
            for item in self.iterable:
                if item < min_val:
                    min_val = item
            return min_val
        except StopIteration:
            return None

if __name__ == '__main__':
    sample_list = [34, 56, 23, 89, 12, 78]
    finder = MinFinder(sample_list)
    minimum = finder.find_min()
    print(minimum)