def safe_first_element(iterable):
    try:
        return next(iter(iterable))
    except (TypeError, StopIteration):
        return None

class SafeIterableProcessor:
    def __init__(self, iterable):
        self.iterable = iterable

    def get_first_element(self):
        return safe_first_element(self.iterable)

if __name__ == '__main__':
    sample_values = [
        [1, 2, 3],
        (4, 5, 6),
        "hello",
        {'a': 1, 'b': 2},
        {7, 8, 9},
        []
    ]

    for value in sample_values:
        processor = SafeIterableProcessor(value)
        print(f"First element of {type(value).__name__}: {processor.get_first_element()}")