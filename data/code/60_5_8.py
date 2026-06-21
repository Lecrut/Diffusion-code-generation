class LastItemGenerator:
    def __init__(self, iterable):
        self.iterable = iterable

    def generate(self):
        last_item = None
        for item in self.iterable:
            last_item = item
        if last_item is not None:
            yield last_item

if __name__ == '__main__':
    sample_iterable = [100, 200, 300, 400, 500]
    generator = LastItemGenerator(sample_iterable)
    for last_item in generator.generate():
        print(last_item)