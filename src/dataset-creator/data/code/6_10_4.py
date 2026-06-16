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
    assert not comparator.is_strictly_greater(5, "5")
    assert not comparator.is_strictly_greater("5", 5)
    assert comparator.is_strictly_greater(10, 9)
    assert not comparator.is_strictly_greater(9, 10)
    assert not comparator.is_strictly_greater(None, None)
    print("All tests passed.")