class BooleanComparator:
    def __init__(self, attr1: bool, attr2: bool):
        self.attr1 = attr1
        self.attr2 = attr2

    def validate_inputs(self, a: bool, b: bool) -> None:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Both inputs must be boolean values.")

    def check_equality(self, a: bool, b: bool) -> bool:
        self.validate_inputs(a, b)
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator(True, False)
    print(comparator.check_equality(True, True))
    print(comparator.check_equality(True, False))
    print(comparator.check_equality(False, True))
    print(comparator.check_equality(False, False))