class Calculator:
    def add(self, a: int, b: int) -> int:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both inputs must be numbers")
        return a + b

if __name__ == '__main__':
    calc = Calculator()
    result1 = calc.add(3, 5)
    result2 = calc.add(7.5, 9.2)
    print(result1)
    print(result2)