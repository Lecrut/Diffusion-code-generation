class BooleanComparator:
    @staticmethod
    def are_equivalent(a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    print(BooleanComparator.are_equivalent(True, True))
    print(BooleanComparator.are_equivalent(True, False))
    print(BooleanComparator.are_equivalent(False, True))
    print(BooleanComparator.are_equivalent(False, False))