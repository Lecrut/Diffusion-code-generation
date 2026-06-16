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
    assert comparator.is_strictly_greater(5, 3) is True
    assert comparator.is_strictly_greater("b", "a") is True
    assert comparator.is_strictly_greater([1, 2], [0, 1]) is True
    assert comparator.is_strictly_greater(5, "3") is False
    assert comparator.is_strictly_greater("b", 1) is False
    try:
        result = comparator.is_strictly_greater(None, None)
        assert result is False
    except Exception:
        pass
    print("All tests passed.")