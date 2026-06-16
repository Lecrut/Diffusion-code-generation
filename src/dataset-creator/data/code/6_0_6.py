class NumericComparator:
    def is_strictly_greater(self, value1, value2):
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise TypeError("Both values must be numeric.")
        try:
            return value1 > value2
        except Exception as e:
            raise ValueError(f"Comparison failed due to invalid operation: {e}")
if __name__ == '__main__':
    comparator = NumericComparator()
    test_cases = [
        (5, 3),
        (5.0, 4.9),
        ("10", "2"),
        (-1, -5),
        (float('inf'), float('-inf')),
    ]
    for val1, val2 in test_cases:
        try:
            result = comparator.is_strictly_greater(val1, val2)
            print(f"{val1} > {val2}: {result}")
        except TypeError as te:
            print(f"TypeError for ({val1}, {val2}): {te}")
        except ValueError as ve:
            print(f"ValueError for ({val1}, {val2}): {ve}")