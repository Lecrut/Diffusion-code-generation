class Calculator:
    def sum_three(self, a, b, c):
        return a + b + c

if __name__ == '__main__':
    calc = Calculator()
    result = calc.sum_three(10, 20, 30)
    print(result)