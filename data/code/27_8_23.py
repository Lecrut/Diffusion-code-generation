class NumericComparator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def are_inequal(self):
        return self.value1 != self.value2

if __name__ == '__main__':
    comparator = NumericComparator(42, 7)
    print(comparator.are_inequal())