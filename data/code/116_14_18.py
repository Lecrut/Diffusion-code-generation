class Calculator:
    def sum_three(self, a: int, b: int, c: int) -> int:
        return a + b + c

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.sum_three(10, 20, 30)
    result2 = calc.sum_three(5, 15, 25)
    print(result1)
    print(result2)