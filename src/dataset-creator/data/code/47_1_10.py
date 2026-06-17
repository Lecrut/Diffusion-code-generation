class IntegerMultiplier:
    def __init__(self, first_value: int = None, second_value: int = None) -> None:
        self.first_value = first_value if first_value is not None else 5
        self.second_value = second_value if second_value is not None else 10
        _validate_integer(self.first_value)
        _validate_integer(self.second_value)
    def multiply(self, other_first: int | None = None, other_second: int | None = None) -> int:
        if other_first is None and self.first_value is not None:
            val_a = self.first_value
        else:
            _validate_integer(other_first)
            val_a = other_first
        if other_second is None and self.second_value is not None:
            val_b = self.second_value
        else:
            _validate_integer(other_second)
            val_b = other_second
        return val_a * val_b
def _validate_integer(value: int | float) -> None:
    if isinstance(value, float) and not value.is_integer():
        raise TypeError(f"Value {value} must be a whole number.")
    try:
        integer_value = int(float(value))
    except (TypeError, ValueError):
        raise TypeError(f"Invalid input type for multiplication. Expected int or numeric convertible to int.") from None
    if not (-10**9 < integer_value <= 10**9):
        raise ValueError(f"Value {integer_value} is out of acceptable range [-{10**9}, {10**9}).")
if __name__ == '__main__':
    multiplier = IntegerMultiplier()
    result_1 = multiplier.multiply(3, 4)
    print(f"Product: {result_1}")
    result_2 = multiplier.multiply(-500000000, -7)
    print(f"Large negative product: {result_2}")