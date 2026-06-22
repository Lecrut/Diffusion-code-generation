class ValueComparator:

    def __init__(self, value):
        self.value = value

    def is_greater_than(self, other_value):
        return self.value > other_value
if __name__ == '__main__':
    comparator = ValueComparator(10)
    other_value = 5
    print(comparator.is_greater_than(other_value))
    another_comparator = ValueComparator(3)
    another_other_value = 7
    print(another_comparator.is_greater_than(another_other_value))