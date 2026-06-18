def product(func):
    def wrapper(*args, **kwargs):
        result = 1
        for arg in args:
            result *= arg
        return result
    return wrapper
@product
def multiply_all(*args):
    return args
if __name__ == '__main__':
    print(multiply_all(2, 3, 4))
    print(multiply_all(10, 5))
    print(multiply_all(7))