class PositiveFilter:
    def __init__(self, iterable):
        self.iterable = iterable

    def filter(self):
        for item in self.iterable:
            if item > 0:
                yield True

if __name__ == '__main__':
    sample_values = [-10, -5, 0, 2, 8, -3, 6]
    filter_instance = PositiveFilter(sample_values)
    result = list(filter_instance.filter())
    print(result)