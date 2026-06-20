class Calculator:
    def calculate_difference(self, num1: float, num2: float) -> float:
        if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
            raise TypeError("Both inputs must be numbers")
        return num1 - num2

if __name__ == '__main__':
    calc = Calculator()
    result = calc.calculate_difference(100.5, 45.2)
    print(result)