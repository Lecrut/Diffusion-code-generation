class IntegerComparator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compare(self):
        return self.a == self.b

if __name__ == '__main__':
    comparator1 = IntegerComparator(5, 5)
    print(comparator1.compare())  # True

    comparator2 = IntegerComparator(3, 4)
    print(comparator2.compare())  # False