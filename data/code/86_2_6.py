class BooleanComparator:
    TRUE = True
    FALSE = False

    @staticmethod
    def check_equality(a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.check_equality(BooleanComparator.TRUE, BooleanComparator.TRUE))
    print(comparator.check_equality(BooleanComparator.TRUE, BooleanComparator.FALSE))
    print(comparator.check_equality(BooleanComparator.FALSE, BooleanComparator.TRUE))
    print(comparator.check_equality(BooleanComparator.FALSE, BooleanComparator.FALSE))