class BooleanComparator:
    def compare(self, bool1, bool2):
        return bool1 == bool2

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.compare(True, True))
    print(comparator.compare(True, False))
    print(comparator.compare(False, True))
    print(comparator.compare(False, False))