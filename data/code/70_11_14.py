def get_edge_elements(lst):
    if not lst:
        raise ValueError("Input must be non-empty")
    return (lst[0], lst[-1])

class EdgeExtractor:
    _VALID_TYPES = (list, tuple)

    def __init__(self, data):
        self.data = data

    @staticmethod
    def extract(items):
        if not isinstance(items, EdgeExtractor._VALID_TYPES):
            raise ValueError("Unsupported type")
        if not items:
            raise ValueError("Empty sequence")
        return get_edge_elements(items)

if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    extractor = EdgeExtractor(numbers)
    first_and_last = extractor.extract(numbers)
    print(first_and_last)