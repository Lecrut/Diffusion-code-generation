class Calculator:

    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Both inputs must be numbers')
        return a + b
if __name__ == '__main__':
    calc = Calculator()
    result = calc.add(10, 5)
    print(result)