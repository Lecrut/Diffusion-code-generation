class QuantityCalculator:
    def add(self, quantity1: int, quantity2: int) -> int:
        return quantity1 + quantity2
if __name__ == '__main__':
    calculator = QuantityCalculator()
    a = 10
    b = 25
    result = calculator.add(a, b)
    print(result)