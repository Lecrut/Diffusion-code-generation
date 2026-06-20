class BooleanComparator:
    EQUAL = "Equal"
    NOT_EQUAL = "Not Equal"

    @staticmethod
    def check_equality(a: bool, b: bool) -> str:
        return BooleanComparator.EQUAL if a == b else BooleanComparator.NOT_EQUAL

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.check_equality(True, True))
    print(comparator.check_equality(False, False))
    print(comparator.check_equality(True, False))
    print(comparator.check_equality(False, True))