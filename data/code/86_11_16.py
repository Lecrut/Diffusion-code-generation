class BooleanComparator:
    def check_equality(self, a: bool, b: bool) -> str:
        if a == b:
            return 'Equal'
        else:
            return 'Not Equal'

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.check_equality(True, True))
    print(comparator.check_equality(False, False))
    print(comparator.check_equality(True, False))
    print(comparator.check_equality(False, True))