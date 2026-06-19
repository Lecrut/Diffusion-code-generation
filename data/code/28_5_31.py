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
if __name__ == '__main__':
    result = add(5, 3)
    print(result)
    result = add(2, 4)
    print(result)