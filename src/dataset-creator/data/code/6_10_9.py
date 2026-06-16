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
    assert comparator.is_strictly_greater(4.9, 4.8) is True
    assert comparator.is_strictly_greater(10.5, 10.6) is False
    assert comparator.is_strictly_greater("apple", "banana") is False
    assert comparator.is_strictly_greater("zebra", "ant") is True
    try:
        comparator.is_strictly_greater(10, "20")
        print("ERROR: Expected TypeError for type mismatch.")
    except TypeError as e:
        assert str(e) == "Both values must be of the same type."
    try:
        result = comparator.is_strictly_greater(1+2j, 3+4j)
    except TypeError as e:
        pass
    print("All tests passed.")