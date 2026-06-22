class Calculator:
    def add(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Both inputs must be numbers")
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    try:
        result = calc.add(7.5, 2.3)
        print(result)
    except ValueError as e:
        print(e)