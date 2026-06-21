class PowerCalculator:
    @staticmethod
    def binary_exponentiation(base, exponent):
        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result *= base
            base *= base
            exponent //= 2
        return result

if __name__ == '__main__':
    calculator = PowerCalculator()
    print(calculator.binary_exponentiation(2, 10))