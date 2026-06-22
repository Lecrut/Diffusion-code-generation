class Calculator:
    def add(self, x, y):
        return x + y

if __name__ == '__main__':
    calc = Calculator()
    result = calc.add(3, 5)
    print(result)