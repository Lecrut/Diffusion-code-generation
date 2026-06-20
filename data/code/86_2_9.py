class BooleanComparator:
    def __init__(self, a: bool, b: bool):
        self.a = a
        self.b = b

    def check_equality(self) -> bool:
        if not isinstance(self.a, bool) or not isinstance(self.b, bool):
            raise ValueError("Both inputs must be boolean values.")
        return self.a == self.b

if __name__ == '__main__':
    comparator1 = BooleanComparator(True, True)
    print(f"Equality of {comparator1.a} and {comparator1.b}: {comparator1.check_equality()}")

    comparator2 = BooleanComparator(True, False)
    print(f"Equality of {comparator2.a} and {comparator2.b}: {comparator2.check_equality()}")

    comparator3 = BooleanComparator(False, False)
    print(f"Equality of {comparator3.a} and {comparator3.b}: {comparator3.check_equality()}")

    comparator4 = BooleanComparator(False, True)
    print(f"Equality of {comparator4.a} and {comparator4.b}: {comparator4.check_equality()}")