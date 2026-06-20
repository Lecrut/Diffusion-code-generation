class Calculator:
    def add(self, a: int, b: int) -> int:
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    result = calc.add(15, 27)
    print(result)