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

@match_checker(30)
def subtract(a, b):
    return a - b

class Calculator:
    def __init__(self):
        self.result = 0

    @match_checker(15)
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        self.result = a / b
        return self.result

if __name__ == '__main__':
    try:
        print(subtract(40, 10))
    except ValueError as e:
        print(e)

    calc = Calculator()
    try:
        print(calc.divide(30, 2))
    except (ValueError, ZeroDivisionError) as e:
        print(e)