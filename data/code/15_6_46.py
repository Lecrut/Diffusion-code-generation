MATCH_VALUE = 15

def match_checker(expected_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not isinstance(result, type(expected_value)):
                raise ValueError(f"Result type {type(result)} does not match the expected type {type(expected_value)}")
            if result != expected_value:
                raise ValueError(f"Result {result} does not match the expected value {expected_value}")
            return result
        return wrapper
    return decorator

@match_checker(MATCH_VALUE)
def add(a, b):
    return a + b

class MathOperations:
    @match_checker(MATCH_VALUE)
    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    try:
        print(add(10, 5))
    except ValueError as e:
        print(e)

    calculator = MathOperations()
    try:
        print(calculator.multiply(3, 5))
    except ValueError as e:
        print(e)