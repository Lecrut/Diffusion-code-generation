class BoolComparator:
    def compare(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BoolComparator()
    print(comparator.compare(True, True))
    print(comparator.compare(False, False))
    print(comparator.compare(True, False))