class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.add(3, 5)
    result2 = calc.add(7, 9)
    print(result1)
    print(result2)