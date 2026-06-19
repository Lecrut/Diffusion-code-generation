def is_strictly_greater(func):

    def wrapper(arg1, arg2):
        if arg1 > arg2:
            return func(arg1, arg2)
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
    print(add(5, 3))
    print(add(2, 4))
    print(multiply(6, 2))
    print(multiply(1, 7))