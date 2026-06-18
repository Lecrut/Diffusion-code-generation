class ValueComparator:
    def is_strictly_greater(self, value1, value2):
        if type(value1) != type(value2):
            raise TypeError("Both values must be of the same type.")
        try:
            return value1 > value2
        except TypeError:
            return False
if __name__ == '__main__':
    comparator = ValueComparator()
    assert comparator.is_strictly_greater(5, 3) is True
    assert comparator.is_strictly_greater(3, 5) is False
    assert comparator.is_strictly_greater("apple", "banana") is False
    assert comparator.is_strictly_greater("zebra", "ant") is True
    try:
        comparator.is_strictly_greater(5, "10")
        print("Error expected for type mismatch.")
    except TypeError as e:
        assert str(e) == "Both values must be of the same type."
    assert comparator.is_strictly_greater(3.14, 2.71) is True
    print("All tests passed.")