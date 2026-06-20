class BooleanComparator:
    def compare(self, a, b):
        return (not a) == (not b)

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.compare(True, True))
    print(comparator.compare(False, False))
    print(comparator.compare(True, False))