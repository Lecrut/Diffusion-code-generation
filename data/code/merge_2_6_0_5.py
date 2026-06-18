class NumericComparator:
    def is_strictly_greater(self, value1, value2):
        if not isinstance(value1, (int, float)) or not isinstance(value2, (int, float)):
            raise TypeError("Both inputs must be numeric types.")
        return value1 > value2
if __name__ == '__main__':
    comparator = NumericComparator()
    assert comparator.is_strictly_greater(5, 3) is True
    assert comparator.is_strictly_greater(3.9, 3.8) is True
    assert comparator.is_strictly_greater(10, 5.5) is True
    assert comparator.is_strictly_greater(7, 7) is False
    try:
        comparator.is_strictly_greater("ten", 3)
        print("Test failed: Should have raised TypeError")
    except TypeError as e:
        pass                    
    try:
        comparator.is_strictly_greater(None, None)
        print("Test failed: Should have raised TypeError")
    except TypeError as e:
        pass                    
    print("All tests passed.")