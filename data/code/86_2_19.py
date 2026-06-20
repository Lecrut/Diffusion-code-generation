class BooleanComparator:
    def __init__(self, attr1: bool, attr2: bool):
        self.attr1 = attr1
        self.attr2 = attr2

    def validate_inputs(self) -> None:
        if not isinstance(self.attr1, bool) or not isinstance(self.attr2, bool):
            raise ValueError("Both inputs must be boolean values.")

    def check_equality(self) -> bool:
        self.validate_inputs()
        return self.attr1 == self.attr2

if __name__ == '__main__':
    comparator = BooleanComparator(True, False)
    print(f"Equality of True and False: {comparator.check_equality()}")