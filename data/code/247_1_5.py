class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.add(5, 3)
    print(result1)
    result2 = calc.add(-10, 20)
    print(result2)