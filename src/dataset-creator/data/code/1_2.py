class Calculator:
    def subtract(self, a, b):
        return a - b
if __name__ == '__main__':
    calc = Calculator()
    result = calc.subtract(10, 4)
    print(result)