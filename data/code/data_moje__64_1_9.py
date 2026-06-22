POWER_CONFIG = {
    "strict_int_exponent": True,
    "allow_negative_base": True,
    "allow_zero_exponent": True
}

def validate_input(base, exponent, config):
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    if not config.get("allow_negative_base") and base < 0:
        raise ValueError("Negative base not allowed in this configuration")
    if not config.get("allow_zero_exponent") and exponent == 0:
        raise ValueError("Zero exponent not allowed in this configuration")

def compute_power(base, exponent):
    config = POWER_CONFIG
    validate_input(base, exponent, config)
    return base ** exponent

class PowerCalculator:
    def __init__(self):
        self.config = POWER_CONFIG

    def calculate(self, base, exponent):
        validate_input(base, exponent, self.config)
        return base ** exponent

if __name__ == '__main__':
    calc = PowerCalculator()
    res1 = calc.calculate(5, 3)
    print(res1)
    res2 = calc.calculate(2.5, 4)
    print(res2)
    res3 = calc.calculate(-2, 5)
    print(res3)
    res4 = calc.calculate(10, 0)
    print(res4)