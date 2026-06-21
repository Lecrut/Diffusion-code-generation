def match_checker(expected_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result != expected_value:
                raise ValueError(f"Result {result} does not match the expected value {expected_value}")
            return result
        return wrapper
    return decorator

@match_checker(25)
def square_root(x):
    return x ** 0.5

class MathOperations:
    def __init__(self, base):
        self.base = base
    
    @match_checker(16)
    def power(self, exponent):
        return self.base ** exponent

if __name__ == '__main__':
    try:
        print(square_root(25))
    except ValueError as e:
        print(e)

    calc = MathOperations(4)
    try:
        print(calc.power(2))
    except ValueError as e:
        print(e)