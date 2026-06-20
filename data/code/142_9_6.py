class BooleanComparator:
    @staticmethod
    def are_identical(a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    print(BooleanComparator.are_identical(True, True))
    print(BooleanComparator.are_identical(False, False))
    print(BooleanComparator.are_identical(True, False))