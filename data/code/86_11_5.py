class BooleanComparator:
    EQUAL_MESSAGE = 'Equal'
    NOT_EQUAL_MESSAGE = 'Not Equal'

    def check_equality(self, a: bool, b: bool) -> str:
        return self.EQUAL_MESSAGE if a == b else self.NOT_EQUAL_MESSAGE

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(comparator.check_equality(True, True))
    print(comparator.check_equality(False, False))
    print(comparator.check_equality(True, False))
    print(comparator.check_equality(False, True))