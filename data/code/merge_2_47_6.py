class IntegerProductCalculator:
    def calculate_product(self, a: int, b: int) -> int:
        return a * b
def run_tests():
    calculator = IntegerProductCalculator()
    assert calculator.calculate_product(2, 3) == 6
    assert calculator.calculate_product(-4, -5) == 20
    assert calculator.calculate_product(10, 0) == 0
    print("All tests passed.")
if __name__ == '__main__':
    run_tests()