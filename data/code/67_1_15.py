class Calculator:

    def __init__(self):
        self.operations = {'add': self.add}

    def add(self, a, b):
        return a + b
if __name__ == '__main__':
    calc = Calculator()
    num1 = 7
    num2 = 8
    result = calc.operations['add'](num1, num2)
    print(result)