class BooleanComparator:
    @staticmethod
    def are_equivalent(a: bool, b: bool) -> bool:
        return not (a ^ b)

if __name__ == '__main__':
    print(BooleanComparator.are_equivalent(True, True))
    print(BooleanComparator.are_equivalent(False, False))
    print(BooleanComparator.are_equivalent(True, False))