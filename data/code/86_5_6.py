class BooleanComparator:
    def __init__(self, a: bool, b: bool):
        self.a = a
        self.b = b

    def compare(self) -> tuple:
        return (self.a == self.b), '=='

if __name__ == '__main__':
    comparator1 = BooleanComparator(True, False)
    print(comparator1.compare())

    comparator2 = BooleanComparator(False, False)
    print(comparator2.compare())