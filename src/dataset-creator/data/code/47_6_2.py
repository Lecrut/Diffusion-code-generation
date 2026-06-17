class IntegerProductCalculator:
    def calculate_product(self, num1: int, num2: int) -> int:
        return num1 * num2
def run_tests():
    calculator = IntegerProductCalculator()
    assert calculator.calculate_product(3, 4) == 12
    assert calculator.calculate_product(-5, -6) == 30
    assert calculator.calculate_product(0, 100) == 0
    print("All tests passed.")
if __name__ == '__main__':
    run_tests()