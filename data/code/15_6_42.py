MATCH_VALUE = 25

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

@match_checker(MATCH_VALUE)
def calculate_sum(a, b):
    return a + b

class MathOperations:
    @match_checker(50)
    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    try:
        print(calculate_sum(12, 13))
    except ValueError as e:
        print(e)

    math_ops = MathOperations()
    try:
        print(math_ops.multiply(5, 10))
    except ValueError as e:
        print(e)