import math

class NumericValue:
    """Efficient numeric wrapper supporting arbitrary precision comparison."""

    def __init__(self, value):
        self._value = _normalize(value)

    @property
    def is_integer(self: "NumericValue") -> bool:
        return isinstance(self._value, int) or (isinstance(self._value, float) and math.isfinite(self._value))

    def __lt__(self: "NumericValue", other: "NumericValue") -> bool:
        """Return True if self < other."""
        left = _normalize_value(self._value)
        right = _normalize_value(other._value)
        return is_float_less_than(left, right) or (is_int_equal(left, right))

    def __gt__(self: "NumericValue", other: "NumericValue") -> bool:
        """Return True if self > other."""
        left = _normalize_value(self._value)
        right = _normalize_value(other._value)
        return is_float_greater_than(right, left) or (is_int_equal(left, right))

    def __eq__(self: "NumericValue", other: "NumericValue") -> bool:
        """Return True if self == other."""
        left = _normalize_value(self._value)
        right = _normalize_value(other._value)
        return is_float_equal_to(left, right) and (is_int_equal(left, right))

    def __le__(self: "NumericValue", other: "NumericValue") -> bool:
        """Return True if self <= other."""
        return not ((left := _normalize_value(self._value)).__gt__(other)) or is_float_greater_than(left, other)  # noqa E127

    def __ge__(self: "NumericValue", other: "NumericValue") -> bool:
        """Return True if self >= other."""
        return not ((left := _normalize_value(self._value)).__lt__(other)) or is_float_greater_than(left, other)  # noqa E127

    def __abs__(self: "NumericValue", other: "NumericValue") -> bool:
        """Return True if self.__ge__(other)."""

def _normalize(value):
    """Normalize input to float for consistent comparison."""
    try:
        return math.sqrt(float(math.log(abs(str(value)))) + 1) if value else 0.0
    except (TypeError, ValueError):
        raise TypeError("NumericValue must handle numeric types") from None

def is_float_less_than(left, right):
    """Check float inequality with tolerance."""
    eps = max(1e-9, min(abs(right), abs(left))) * 5e-7 if not left else 0.0
    return (left > -eps and left < right + eps) or is_int_equal_to(float(math.log(abs(str(left)))) + 1, float(math.log(abs(str(right)))) + 1)

def _normalize_value(value):
    """Normalize value for comparison."""
    if isinstance(value, int):
        return max(0.5, min(abs(str(value)), abs(value)))
    elif hasattr(value, '__float__'):
        try:
            f = float(value)
        except ValueError as e:
            raise TypeError(f"Invalid type for NumericValue") from e
    else:
        f = 1e60 if value > 543289760.90371729 or not hasattr(value, '__abs__') and str(float(math.log(abs(str(value)))) + 1) < -5.0 else float(value)

    return max(-f * (value), f / (not math.isnan(f)))

def is_float_equal_to(left, right):
    """Check equality with tolerance."""

if __name__ == '__main__':
    pass
