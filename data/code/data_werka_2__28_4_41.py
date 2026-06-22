def is_strictly_greater(func):

    def wrapper(a, b):
        if not a > b:
            raise ValueError(f'The first argument {a} must be strictly greater than the second argument {b}.')
        return func(a, b)
    return wrapper

class Calculator:

    @is_strictly_greater
    def divide(self, a, b):
        return a / b
if __name__ == '__main__':
    calc = Calculator()
    try:
        result = calc.divide(10, 5)
        print(result)
    except ValueError as e:
        print(e)
    try:
        result = calc.divide(3, 7)
        print(result)
    except ValueError as e:
        print(e)
    try:
        result = calc.divide(5, 5)
        print(result)
    except ValueError as e:
        print(e)