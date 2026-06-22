class PowerCalculator:
    ZERO_EXPONENT_RESULT = 1.0
    INVALID_ZERO_BASE_NEGATIVE_EXP = "Base zero with negative exponent is undefined"

    @staticmethod
    def _validate_inputs(base, exponent):
        if base == 0 and exponent < 0:
            raise ValueError(PowerCalculator.INVALID_ZERO_BASE_NEGATIVE_EXP)

    @staticmethod
    def _binary_exponentiation_positive(base, exp):
        result = PowerCalculator.ZERO_EXPONENT_RESULT
        current_base = base
        while exp > 0:
            if exp & 1:
                result *= current_base
            current_base *= current_base
            exp >>= 1
        return result

    @staticmethod
    def calculate_power(base, exponent):
        PowerCalculator._validate_inputs(base, exponent)
        if exponent == 0:
            return PowerCalculator.ZERO_EXPONENT_RESULT
        is_negative = exponent < 0
        abs_exponent = abs(exponent)
        result = PowerCalculator._binary_exponentiation_positive(base, abs_exponent)
        if is_negative:
            result = 1.0 / result
        return result

if __name__ == '__main__':
    calculator = PowerCalculator()
    print(calculator.calculate_power(2, 10))
    print(calculator.calculate_power(5, 0))
    print(calculator.calculate_power(2, -2))
    print(calculator.calculate_power(3.5, 2))
    print(calculator.calculate_power(10, -3))