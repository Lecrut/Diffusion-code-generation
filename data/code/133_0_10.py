class IntegerComparator:
    def __init__(self, value):
        self.value = value

    def compare_to(self, other):
        return self.value == other.value

if __name__ == '__main__':
    comparator1 = IntegerComparator(10)
    comparator2 = IntegerComparator(10)
    print(comparator1.compare_to(comparator2))  # True
    comparator3 = IntegerComparator(5)
    print(comparator1.compare_to(comparator3))  # False