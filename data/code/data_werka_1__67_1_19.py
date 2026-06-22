class Calculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    numbers = {'first': 7, 'second': 12}
    result = calc.add(numbers['first'], numbers['second'])
    print(result)