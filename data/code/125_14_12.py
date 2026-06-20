class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

if __name__ == '__main__':
    calc = Calculator()
    assert calc.add(2, 3) == 5, "Addition test failed"
    assert calc.subtract(5, 2) == 3, "Subtraction test failed"
    print("Addition of 2 and 3 is:", calc.add(2, 3))
    print("Subtraction of 5 and 2 is:", calc.subtract(5, 2))