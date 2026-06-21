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
def add_and_multiply(a, b):
    return (a + b) * 2

class MathOperations:
    def __init__(self):
        self.results = {}

    @match_checker(36)
    def square(self, x):
        return x * x

    def store_result(self, key, value):
        self.results[key] = value

if __name__ == '__main__':
    try:
        print(add_and_multiply(4, 6))
    except ValueError as e:
        print(e)

    math_ops = MathOperations()
    try:
        result = math_ops.square(6)
        print(result)
        math_ops.store_result('square_of_6', result)
    except ValueError as e:
        print(e)

    print(math_ops.results)