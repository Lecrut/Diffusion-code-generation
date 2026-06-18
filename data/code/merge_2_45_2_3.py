class Calculator:
    def total(self, value1: float, value2: float) -> float:
        return value1 + value2
if __name__ == '__main__':
    calc = Calculator()
    result_a = calc.total(10, 5)
    print(f"Total A: {result_a}")
    result_b = calc.total(-3.5, 7.2)
    print(f"Total B: {result_b}")