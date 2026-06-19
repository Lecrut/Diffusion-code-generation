class Calculator:
    def add(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both inputs must be numbers")
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    num1 = 7
    num2 = 8
    result = calc.add(num1, num2)
    print(result)