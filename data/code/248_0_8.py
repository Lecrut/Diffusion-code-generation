class Calculator:
    def add_two_integers(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Both arguments must be integers")
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.add_two_integers(42, 17)
    result2 = calc.add_two_integers(3, 5)
    print(result1)
    print(result2)