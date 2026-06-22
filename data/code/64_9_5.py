class PowerCalculator:
    def calculate(self, base, exponent):
        return base ** exponent

if __name__ == "__main__":
    calculator = PowerCalculator()
    print(calculator.calculate(5, 2))
    print(calculator.calculate(3, 4))