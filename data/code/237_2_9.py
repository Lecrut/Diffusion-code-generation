class PowerOfTwoCalculator:
    def __init__(self):
        self.powers = [1 << i for i in range(10)]

    def get_powers(self):
        return self.powers

if __name__ == '__main__':
    calculator = PowerOfTwoCalculator()
    result = calculator.get_powers()
    print(result)