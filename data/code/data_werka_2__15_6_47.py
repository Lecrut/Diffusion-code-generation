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

@match_checker(25)
def square_root(a):
    import math
    return int(math.sqrt(a))

class MathOperations:
    def __init__(self):
        self.results = []

    @match_checker(18)
    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    try:
        print(square_root(625))
    except ValueError as e:
        print(e)

    math_ops = MathOperations()
    try:
        print(math_ops.multiply(9, 2))
    except ValueError as e:
        print(e)