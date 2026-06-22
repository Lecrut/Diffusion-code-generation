def is_strictly_greater(func):

    def wrapper(a, b, *args, **kwargs):
        if a > b:
            return func(a, b, *args, **kwargs)
        else:
            return None
    return wrapper

@is_strictly_greater
def add(a, b):
    return a + b

@is_strictly_greater
def multiply(a, b):
    return a * b
if __name__ == '__main__':
    result_add = add(10, 5)
    print(result_add)
    result_multiply = multiply(7, 3)
    print(result_multiply)
    invalid_add = add(3, 5)
    print(invalid_add)
    invalid_multiply = multiply(2, 4)
    print(invalid_multiply)