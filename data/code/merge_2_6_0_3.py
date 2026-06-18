class NumericComparator:
    def is_strictly_greater(self, value1, value2):
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise TypeError("Both values must be numeric.")
        return value1 > value2
if __name__ == '__main__':
    comparator = NumericComparator()
    test_cases = [
        ((5.0, 3), True),
        ((-1, -5), True),
        ((10, 10), False),
        (("a", 2), TypeError),
        ((None, 4), TypeError),
        ((3.5, "b"), TypeError)
    ]
    for val1, val2 in test_cases:
        try:
            result = comparator.is_strictly_greater(val1[0], val1[1]) if isinstance(val1, tuple) else comparator.is_strictly_greater(*val1)
            print(f"Comparison {val1}: Result is {result}")
        except TypeError as e:
            print(f"Error for input {val1}: {e}")