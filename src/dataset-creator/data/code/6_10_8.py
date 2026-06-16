class ValueComparator:
    def is_strictly_greater(self, value1, value2):
        if type(value1) != type(value2):
            raise TypeError("Both values must be of the same type.")
        try:
            return value1 > value2
        except TypeError as e:
            raise TypeError(f"Comparison operation failed for types {type(value1).__name__}: {e}")
if __name__ == '__main__':
    comparator = ValueComparator()
    assert comparator.is_strictly_greater(5, 3) is True
    assert comparator.is_strictly_greater(2, 7) is False
    assert comparator.is_strictly_greater(10.5, 9.8) is True
    assert comparator.is_strictly_greater(4.2, 4.3) is False
    try:
        result = comparator.is_strictly_greater("10", "5")
        print(f"Unexpected success for strings: {result}")
    except TypeError as e:
        pass
    print("All tests passed.")