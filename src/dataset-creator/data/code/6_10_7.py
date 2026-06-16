class ValueComparator:
    def is_strictly_greater(self, value1, value2):
        if type(value1) != type(value2):
            return False
        try:
            return value1 > value2
        except TypeError:
            return False
if __name__ == '__main__':
    comparator = ValueComparator()
    test_cases = [
        (5, 3),
        ("apple", "banana"),
        ([1], [0]),
        ((1,), ()),
        (True, True)
    ]
    for val1, val2 in test_cases:
        result = comparator.is_strictly_greater(val1, val2)
        print(f"{val1} > {val2}: {result}")