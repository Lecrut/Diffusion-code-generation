class Calculator:

    def add_numbers(self, a, b):
        return a + b
if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.add_numbers(5, 3)
    result2 = calc.add_numbers(10, 7)
    print(result1)
    print(result2)