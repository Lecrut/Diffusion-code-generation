class Calculator:
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both arguments must be numbers")
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(10, 5))
    print(calc.add(-3, -7))
    print(calc.add(0, 0))
    try:
        print(calc.add('a', 3))
    except ValueError as e:
        print(e)