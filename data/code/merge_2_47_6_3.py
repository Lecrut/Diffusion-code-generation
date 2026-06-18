class IntegerProductCalculator:
    def multiply(self, a: int, b: int) -> int:
        return a * b
def test_multiply():
    calculator = IntegerProductCalculator()
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-4, -5) == 20
    assert calculator.multiply(10, 0) == 0
    print("All unit tests passed.")
if __name__ == '__main__':
    test_multiply()