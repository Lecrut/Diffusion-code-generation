class Calculator:
    def total(self, a, b):
        return a + b
if __name__ == '__main__':
    calc = Calculator()
    result = calc.total(10.5, 20)
    print(result)