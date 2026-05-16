class BooleanComparator:
    def check_equality(self, a: bool, b: bool) -> bool:
        return a == b
if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.check_equality(True, True))
    print(comparator.check_equality(True, False))
    print(comparator.check_equality(False, True))
    print(comparator.check_equality(False, False))