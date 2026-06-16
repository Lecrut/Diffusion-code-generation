def multiply_by_constant(factor):
    def decorator(func):
        def wrapper(*args):
            result = 1
            for arg in args:
                result *= arg
            return result * factor
        return wrapper
    return decorator
@multiply_by_constant(2)
def multiply_all(a, b, c):
    return a + b + c
if __name__ == '__main__':
    print(multiply_all(1, 2, 3))