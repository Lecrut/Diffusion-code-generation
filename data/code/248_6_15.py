class Calculator:
    def add(self, a, b):
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.add(3, 5)
    print(f"The sum of 3 and 5 is: {result1}")
    result2 = calc.add(-2, 4)
    print(f"The sum of -2 and 4 is: {result2}")