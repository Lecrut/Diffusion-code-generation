class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b
if __name__ == '__main__':
    calc = Calculator()
    result = calc.add(10, 25)
    print(result)