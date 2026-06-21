class BooleanComparator:
    def are_equivalent(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.are_equivalent(True, True))
    print(comparator.are_equivalent(True, False))
    print(comparator.are_equivalent(False, True))
    print(comparator.are_equivalent(False, False))