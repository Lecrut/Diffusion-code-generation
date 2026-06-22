class IntegerComparator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compare(self):
        if self.a > self.b:
            return "greater than"
        elif self.a < self.b:
            return "less than"
        else:
            return "equal to"

if __name__ == '__main__':
    comparator = IntegerComparator(10, 5)
    print(comparator.compare())