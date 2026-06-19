class Calculator:

    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both inputs must be numbers')
        return a + b
if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.add(5, 3)
    result2 = calc.add(-5, -3)
    result3 = calc.add(10, -4)
    result4 = calc.add(0, 7)
    result5 = calc.add(-5, 0)
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)