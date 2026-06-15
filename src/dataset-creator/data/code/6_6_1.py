def product_decorator(func):
    def wrapper(*args):
        result = 1
        for arg in args:
            result *= arg
        return func(*args)
    return wrapper
@product_decorator
def multiply(a, b, c):
    return a * b * c
if __name__ == '__main__':
    result = multiply(2, 3, 4)
    print(result)