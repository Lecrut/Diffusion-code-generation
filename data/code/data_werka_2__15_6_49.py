def match_checker(expected_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == expected_value:
                return result
            else:
                raise ValueError(f"Result {result} does not match the expected value {expected_value}")
        return wrapper
    return decorator

class MathOperations:
    def __init__(self):
        self.result = 0

    @match_checker(15)
    def add(self, a, b):
        return a + b

    @match_checker(5)
    def subtract(self, a, b):
        return a - b

    @match_checker(20)
    def multiply(self, a, b):
        return a * b

    @match_checker(2)
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a // b

if __name__ == '__main__':
    calc = MathOperations()
    try:
        print(calc.add(10, 5))
        print(calc.subtract(10, 5))
        print(calc.multiply(4, 5))
        print(calc.divide(10, 5))
    except ValueError as e:
        print(e)