class LastItemGenerator:
    def __init__(self, iterable):
        self.iterable = iterable

    def get_last_item(self):
        last_item = None
        for item in self.iterable:
            last_item = item
        return last_item

if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    generator_instance = LastItemGenerator(sample_iterable)
    print(generator_instance.get_last_item())