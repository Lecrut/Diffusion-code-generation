class Calculator:
    ADDITION_FACTOR = 1

    def add(self, a, b):
        return (a + b) * self.ADDITION_FACTOR

if __name__ == '__main__':
    num1 = 7
    num2 = 8
    calc = Calculator()
    result = calc.add(num1, num2)
    print(result)