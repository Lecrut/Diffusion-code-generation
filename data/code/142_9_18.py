class BooleanComparator:

    def __init__(self, a: bool, b: bool):
        self.a = a
        self.b = b

    def are_identical(self) -> bool:
        return self.a == self.b
if __name__ == '__main__':
    comparator1 = BooleanComparator(True, True)
    print(comparator1.are_identical())
    comparator2 = BooleanComparator(False, False)
    print(comparator2.are_identical())
    comparator3 = BooleanComparator(True, False)
    print(comparator3.are_identical())