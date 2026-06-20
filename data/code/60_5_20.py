class LastItemGenerator:

    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.last_item = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.last_item is not None:
            item = self.last_item
            self.last_item = None
            return item
        else:
            try:
                while True:
                    self.last_item = next(self.iterable)
            except StopIteration:
                if self.last_item is not None:
                    return self.last_item
                else:
                    raise
if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    generator = LastItemGenerator(sample_iterable)
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))
    print(next(generator))