class ValueComparator:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        return self.value > other_value
if __name__ == '__main__':
    comparator1 = ValueComparator(10)
    comparator2 = ValueComparator(5)
    result = comparator1.is_greater_than(comparator2.value)
    print(result)
    comparator3 = ValueComparator(3)
    result2 = comparator2.is_greater_than(comparator3.value)
    print(result2)