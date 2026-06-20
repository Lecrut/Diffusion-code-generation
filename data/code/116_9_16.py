class Calculator:
    def sum_three(self, a, b, c):
        try:
            return a + b + c
        except TypeError:
            raise ValueError("All inputs must be numeric (int or float) to calculate the sum.")

if __name__ == '__main__':
    calc = Calculator()
    print(calc.sum_three(10, 5.5, 2))
    print(calc.sum_three("hello", 5, 2))
    print(calc.sum_three(3.14, "pi", 1))