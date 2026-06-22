class LastElementGenerator:
    def __init__(self, iterable):
        self.iterable = iterable

    def generate(self):
        last = None
        for item in self.iterable:
            last = item
        if last is not None:
            yield last

if __name__ == '__main__':
    sample_sequence = range(1000000)
    generator_instance = LastElementGenerator(sample_sequence)
    print(next(generator_instance.generate()))