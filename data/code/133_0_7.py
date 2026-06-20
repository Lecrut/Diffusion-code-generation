class IntegerComparator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def compare(self):
        return self.value1 == self.value2

if __name__ == '__main__':
    comparator = IntegerComparator(5, 5)
    print(comparator.compare())  # True