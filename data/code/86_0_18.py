class BoolComparator:
    def __init__(self, a: bool, b: bool):
        self.a = a
        self.b = b

    def compare(self) -> str:
        return "True" if self.a == self.b else "False"

if __name__ == '__main__':
    comparator1 = BoolComparator(True, False)
    print(comparator1.compare())
    comparator2 = BoolComparator(False, False)
    print(comparator2.compare())
    comparator3 = BoolComparator(True, True)
    print(comparator3.compare())