class PowerCalculator:
    EXPONENT_OPERATOR = "**"

    @staticmethod
    def compute(base, exponent):
        return base ** exponent

if __name__ == "__main__":
    base_value = 5
    exp_value = 4
    calculated = PowerCalculator.compute(base_value, exp_value)
    print(calculated)