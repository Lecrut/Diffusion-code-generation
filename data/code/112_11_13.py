class Calculator:
    def add_two_numbers(self, a: float, b: float) -> float:
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.add_two_numbers(5.5, 4.5)
    print(result1)
    result2 = calc.add_two_numbers(-10.2, 3.8)
    print(result2)