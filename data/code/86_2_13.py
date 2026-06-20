class BooleanComparator:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def check_equality(self):
        return self.attr1 == self.attr2

if __name__ == '__main__':
    comparator = BooleanComparator(True, False)
    print(comparator.check_equality())