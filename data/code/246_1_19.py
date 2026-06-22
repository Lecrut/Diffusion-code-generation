class Calculator:
    def add_values(self, a, b):
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    print(calc.add_values(3, 5))
    print(calc.add_values(-7, 12))