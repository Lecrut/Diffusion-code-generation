def check_zero_result(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            print('The result is zero.')
        return result
    return wrapper

@check_zero_result
def add(a, b):
    return a + b

@check_zero_result
def multiply(x, y):
    return x * y
if __name__ == '__main__':
    print(add(5, 3))
    print(multiply(4, 0))