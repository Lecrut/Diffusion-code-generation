class BooleanComparator:
    def __init__(self, attr1: bool, attr2: bool):
        self.attr1 = attr1
        self.attr2 = attr2

    def check_equality(self) -> bool:
        return self.attr1 == self.attr2

if __name__ == '__main__':
    comparator = BooleanComparator(True, False)
    print(comparator.check_equality())