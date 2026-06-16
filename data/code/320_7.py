def subtract_constant(constant):
    def decorator(func):
        def wrapper(*args):
            result = 0
            for arg in args:
                result += arg - constant
            return result
        return wrapper
    return decorator
@subtract_constant(5)
def add_numbers(a, b):
    return a + b
@subtract_constant(10)
def multiply_numbers(a, b):
    return a * b
if __name__ == '__main__':
    print(add_numbers(3, 4))
    print(multiply_numbers(2, 5))