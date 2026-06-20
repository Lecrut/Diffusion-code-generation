class BooleanComparator:
    @staticmethod
    def are_identical(a: bool, b: bool) -> bool:
        return not (a ^ b)

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.are_identical(True, True))
    print(comparator.are_identical(False, False))
    print(comparator.are_identical(True, False))
    print(comparator.are_identical(False, True))