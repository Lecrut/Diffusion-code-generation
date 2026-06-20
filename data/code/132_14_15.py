class XorCalculator:
    def calculate_xor(self, a: bool, b: bool) -> bool:
        return (a + b) % 2 == 1

if __name__ == '__main__':
    calculator = XorCalculator()
    print(calculator.calculate_xor(True, False))
    print(calculator.calculate_xor(False, True))
    print(calculator.calculate_xor(True, True))
    print(calculator.calculate_xor(False, False))