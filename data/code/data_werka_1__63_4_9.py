class FirstElementGenerator:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.first_yielded = False

    def __iter__(self):
        return self

    def __next__(self):
        if not self.first_yielded:
            self.first_yielded = True
            try:
                return next(self.iterable)
            except StopIteration:
                raise ValueError("The iterable is empty")
        else:
            raise StopIteration

if __name__ == '__main__':
    sample_iterable = [7, 14, 21, 28, 35]
    generator = FirstElementGenerator(sample_iterable)
    print(next(generator))