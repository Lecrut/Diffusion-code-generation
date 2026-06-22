def is_strictly_greater(func):

    def wrapper(arg1, arg2):
        if arg1 > arg2:
            return func(arg1, arg2)
        else:
            return None
    return wrapper

@is_strictly_greater
def subtract(a, b):
    return a - b
if __name__ == '__main__':
    result = subtract(10, 5)
    print(result)
    result = subtract(3, 7)
    print(result)