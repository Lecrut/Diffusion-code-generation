class Calculator:
    def add(self, a, b):
        if not all(isinstance(i, (int, float)) for i in [a, b]):
            raise ValueError("Both inputs must be numbers")
        return a + b

    def subtract(self, a, b):
        if not all(isinstance(i, (int, float)) for i in [a, b]):
            raise ValueError("Both inputs must be numbers")
        return a - b

if __name__ == '__main__':
    calc = Calculator()
    print(calc.add(5, 3))
    print(calc.subtract(10, 4))