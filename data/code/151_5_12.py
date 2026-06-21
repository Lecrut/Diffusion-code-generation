class ListCombiner:
    def __init__(self, list_a, list_b):
        self.list_a = iter(list_a)
        self.list_b = iter(list_b)

    def combine(self):
        while True:
            try:
                yield next(self.list_a)
            except StopIteration:
                try:
                    yield next(self.list_b)
                except StopIteration:
                    break

if __name__ == '__main__':
    combiner = ListCombiner([1, 2, 3], [4, 5, 6])
    print(list(combiner.combine()))