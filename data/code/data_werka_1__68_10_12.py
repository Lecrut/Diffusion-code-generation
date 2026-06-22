class NumberComparator:
    def __init__(self, attributes: dict):
        self.attributes = attributes

    def calculate_difference(self) -> int:
        return abs(self.attributes['first'] - self.attributes['second'])

if __name__ == '__main__':
    sample_values = {'first': 15, 'second': 8}
    comparator = NumberComparator(sample_values)
    print(comparator.calculate_difference())