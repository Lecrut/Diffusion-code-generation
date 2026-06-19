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
if __name__ == '__main__':
    result1 = add(10, 5)
    result2 = add(3, 7)
    print(result1)
    print(result2)