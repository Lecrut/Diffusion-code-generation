class Calculator:
    def add_two_numbers(self, a: float, b: float) -> float:
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.add_two_numbers(5.0, 3.0)
    print(result1)
    result2 = calc.add_two_numbers(-10.0, 20.0)
    print(result2)