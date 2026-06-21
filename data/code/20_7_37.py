def check_eq(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, tuple) or len(result) != 2:
            raise ValueError('Function must return a tuple with two elements.')
        a, b = result
        if a is not b:
            raise AssertionError(f'Strict equality check failed: {a} is not {b}')
        return (a, b)
    return wrapper

@check_eq
def add_and_check(x, y):
    return (x + y, x + y)

@check_eq
def multiply_and_check(x, y):
    return (x * y, x * y)

class Calculator:

    def __init__(self, initial_value=0):
        self.value = initial_value

    @check_eq
    def add(self, x):
        return (self.value + x, self.value + x)

    @check_eq
    def multiply(self, x):
        return (self.value * x, self.value * x)
if __name__ == '__main__':
    try:
        print(add_and_check(2, 3))
        print(multiply_and_check(4, 5))
        calc = Calculator(10)
        print(calc.add(5))
        print(calc.multiply(2))
    except (ValueError, AssertionError) as e:
        print(e)