class Calculator:
    def sum_three(self, a, b, c):
        return a + b + c

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.sum_three(1, 2, 3)
    print(result1)
    result2 = calc.sum_three(4, 5, 6)
    print(result2)