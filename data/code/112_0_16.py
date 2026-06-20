class ArithmeticOperations:
    def __init__(self):
        self.num1 = 15
        self.num2 = 27

    def add_numbers(self):
        return self.num1 + self.num2

if __name__ == '__main__':
    calc = ArithmeticOperations()
    result = calc.add_numbers()
    print(result)