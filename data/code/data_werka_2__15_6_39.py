def match_checker(expected_value):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == expected_value:
                return result
            else:
                raise ValueError(f'Result {result} does not match the expected value {expected_value}')
        return wrapper
    return decorator

@match_checker(20)
def sum_of_squares(a, b):
    return a ** 2 + b ** 2

class MathOperations:

    def __init__(self):
        self.value = 0

    @match_checker(10)
    def multiply_by_two(self, num):
        return num * 2
if __name__ == '__main__':
    try:
        print(sum_of_squares(3, 4))
    except ValueError as e:
        print(e)
    calc = MathOperations()
    try:
        print(calc.multiply_by_two(5))
    except ValueError as e:
        print(e)