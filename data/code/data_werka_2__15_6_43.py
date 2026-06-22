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

@match_checker(20)
def sum_of_squares(a, b):
    return a**2 + b**2

class MathOperations:
    def __init__(self):
        self.value = 10

    @match_checker(5)
    def modulo(self, other):
        return self.value % other

if __name__ == '__main__':
    try:
        print(sum_of_squares(3, 4))
    except ValueError as e:
        print(e)

    math_ops = MathOperations()
    try:
        print(math_ops.modulo(6))
    except ValueError as e:
        print(e)