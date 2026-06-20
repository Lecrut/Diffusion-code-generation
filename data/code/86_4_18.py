class PairComparator:
    def __init__(self):
        self.prev = None

    def compare(self, curr):
        result = (self.prev, curr) == (True, True)
        self.prev = curr
        return result

if __name__ == '__main__':
    comparator = PairComparator()
    sample_values = [True, False, True, True, False]
    for value in sample_values:
        print(comparator.compare(value))