def is_strictly_greater(func):
    def wrapper(a, b):
        if not (a > b):
            raise ValueError(f'The first argument {a} must be strictly greater than the second argument {b}.')
        return func(a, b)
    return wrapper

@is_strictly_greater
def divide(a, b):
    return a / b

class Calculator:
    def __init__(self, initial_value):
        self.value = initial_value

    @is_strictly_greater
    def add(self, a, b):
        return a + b

    @is_strictly_greater
    def multiply(self, a, b):
        return a * b

if __name__ == '__main__':
    try:
        result = divide(10, 5)
        print(result)
    except ValueError as e:
        print(e)

    try:
        result = divide(3, 4)
        print(result)
    except ValueError as e:
        print(e)

    calc = Calculator(100)
    try:
        result = calc.add(200, 50)
        print(result)
    except ValueError as e:
        print(e)

    try:
        result = calc.multiply(75, 25)
        print(result)
    except ValueError as e:
        print(e)

    try:
        result = calc.add(50, 100)
        print(result)
    except ValueError as e:
        print(e)