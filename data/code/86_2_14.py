class BooleanComparator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def check_equality(self):
        return self.value1 == self.value2

if __name__ == '__main__':
    comparator = BooleanComparator(True, False)
    print(comparator.check_equality())