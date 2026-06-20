class LastItemGenerator:
    @staticmethod
    def generate_last_item(iterable):
        last_item = None
        for item in iterable:
            last_item = item
        yield last_item

if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    generator = LastItemGenerator.generate_last_item(sample_iterable)
    print(next(generator))