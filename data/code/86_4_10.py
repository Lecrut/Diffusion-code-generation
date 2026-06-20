class PairComparator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.prev = next(self.iterator, None)

    def compare_next_pair(self):
        try:
            curr = next(self.iterator)
            result = (self.prev, curr) == (True, True)
            self.prev = curr
            return result
        except StopIteration:
            return False

if __name__ == '__main__':
    comparator = PairComparator([True, False, True, True, False])
    print(comparator.compare_next_pair())
    print(comparator.compare_next_pair())
    print(comparator.compare_next_pair())
    print(comparator.compare_next_pair())
    print(comparator.compare_next_pair())