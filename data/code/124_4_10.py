class Calculator:

    def add(self, x, y):
        return lambda a, b: a + b(x, y)

    def sub(self, x, y):
        return lambda a, b: a - b(x, y)

    def mul(self, x, y):
        return lambda a, b: a * b(x, y)

    def div(self, x, y):
        return lambda a, b: a / b(x, y)
if __name__ == '__main__':
    calc = Calculator()
    add_result = calc.add(8, 2)
    sub_result = calc.sub(8, 2)
    mul_result = calc.mul(8, 2)
    div_result = calc.div(8, 2)
    print(add_result(10, 2))
    print(sub_result(10, 2))
    print(mul_result(10, 2))
    print(div_result(10, 2))