class NumericValidator:
    def is_strictly_greater(self, a: float | int, b: float | int) -> bool:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both operands must be numeric types.")
        return a > b
if __name__ == '__main__':
    validator = NumericValidator()
    assert validator.is_strictly_greater(5, 3) is True
    assert validator.is_strictly_greater(3.9, 3.8) is True
    assert validator.is_strictly_greater(10, 5.5) is True
    assert validator.is_strictly_greater(5, 5) is False
    print("All assertions passed.")
    try:
        validator.is_strictly_greater("a", "b")
    except TypeError as e:
        pass