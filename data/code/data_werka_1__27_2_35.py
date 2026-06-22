class ValueComparator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def are_values_equal(self):
        return self.a == self.b

    def are_values_different(self):
        return not self.are_values_equal()

if __name__ == '__main__':
    num1 = 42
    num2 = 7
    comparator = ValueComparator(num1, num2)
    print(comparator.are_values_equal())
    print(comparator.are_values_different())