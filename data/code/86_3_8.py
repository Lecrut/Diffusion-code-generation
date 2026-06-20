class BooleanComparator:
    def compare(self, a, b):
        return [a == b]

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.compare(True, False))
    print(comparator.compare(True, True))
    print(comparator.compare(False, True))