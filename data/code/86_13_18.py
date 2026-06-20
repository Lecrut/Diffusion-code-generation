def compare_booleans(a: bool, b: bool) -> bool:
    return a == b

class BooleanComparator:
    def compare(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.compare(True, True))
    print(comparator.compare(False, False))
    print(comparator.compare(True, False))