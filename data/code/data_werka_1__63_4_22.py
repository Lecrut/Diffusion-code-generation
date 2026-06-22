class SingleElementGenerator:

    def __init__(self, iterable):
        self._iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            first_element = next(self._iterator)
            return first_element
        except StopIteration:
            raise ValueError('The iterable is empty')
        finally:
            self._iterator = iter([])
if __name__ == '__main__':
    sample_iterable = [10, 20, 30, 40, 50]
    generator = SingleElementGenerator(sample_iterable)
    print(next(generator))