class BooleanComparator:
    def check_equality(self, a: bool, b: bool) -> str:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Both inputs must be boolean values.")
        return 'Equal' if a == b else 'Not Equal'

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.check_equality(True, True))
    print(comparator.check_equality(False, False))
    print(comparator.check_equality(True, False))
    print(comparator.check_equality(False, True))