class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

if __name__ == '__main__':
    calc = Calculator()
    print(f"Addition: {calc.add(5, 3)}")
    print(f"Subtraction: {calc.subtract(10, 4)}")