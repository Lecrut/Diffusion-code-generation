def _validate_inputs(base, exponent):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be an integer or float")
    if not isinstance(exponent, (int, float)):
        raise TypeError("Exponent must be an integer or float")
    if isinstance(exponent, float) and not exponent.is_integer():
        if base < 0:
            raise ValueError("Negative base with non-integer exponent is invalid")
        if base == 0:
            raise ZeroDivisionError("Zero base with negative exponent is undefined")
    if exponent < 0 and base == 0:
        raise ZeroDivisionError("Cannot raise zero to a negative power")
    if exponent < 0 and base < 0:
        raise ValueError("Negative base with negative exponent is not allowed")

def _calculate_power(base, exponent):
    return base ** exponent

def safe_power(base, exponent):
    _validate_inputs(base, exponent)
    return _calculate_power(base, exponent)

class PowerEngine:
    def __init__(self, base_value, exp_value):
        self.base_value = base_value
        self.exp_value = exp_value

    def compute(self):
        return safe_power(self.base_value, self.exp_value)

if __name__ == '__main__':
    val1 = safe_power(5, 3)
    print(val1)
    val2 = safe_power(10, -2)
    print(val2)
    val3 = safe_power(-4, 4)
    print(val3)
    engine = PowerEngine(2, 5)
    print(engine.compute())
    try:
        safe_power(-2, -3)
    except ValueError as e:
        print(f"Caught error: {e}")