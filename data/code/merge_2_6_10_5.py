class ValueComparator:
    def is_strictly_greater(self, value1: object, value2: object) -> bool:
        if type(value1) != type(value2):
            return False
        try:
            return value1 > value2
        except TypeError:
            return False
if __name__ == '__main__':
    comp = ValueComparator()
    assert not comp.is_strictly_greater(5, 3.0)
    assert comp.is_strictly_greater(6, 4)
    assert not comp.is_strictly_greater("a", "b")
    print("All tests passed.")