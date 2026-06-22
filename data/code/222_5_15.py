class MinFinder:
    def __init__(self, iterable):
        self.iterable = iter(iterable)

    def find_min(self):
        try:
            current_min = next(self.iterable)
        except StopIteration:
            return None

        for item in self.iterable:
            if item < current_min:
                current_min = item
        return current_min

if __name__ == '__main__':
    sample_list = [34, 56, 23, 89, 12, 78]
    finder = MinFinder(sample_list)
    min_value = finder.find_min()
    print(min_value)