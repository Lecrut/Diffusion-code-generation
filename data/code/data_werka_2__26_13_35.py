class IntegerComparator:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        if not isinstance(other_value, int):
            raise ValueError('Other value must be an integer.')
        return self.value > other_value
if __name__ == '__main__':
    comparator1 = IntegerComparator(20)
    comparator2 = IntegerComparator(5)
    print(comparator1.is_greater_than(comparator2.value))
    print(comparator2.is_greater_than(comparator1.value))