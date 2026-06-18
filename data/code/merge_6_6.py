def product_of_args(func):
    def wrapper(*args, **kwargs):
        result = 1
        for arg in args:
            result *= arg
        return result
    return wrapper
@product_of_args
def multiply(a, b, c):
    return a * b * c
if __name__ == '__main__':
    result = multiply(2, 3, 4)
    print(result)