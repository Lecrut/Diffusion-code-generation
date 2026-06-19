def is_strictly_greater(func):

    def wrapper(a, b):
        if a > b:
            return func(a, b)
        else:
            return None
    return wrapper

@is_strictly_greater
def subtract(x, y):
    return x - y
if __name__ == '__main__':
    result1 = subtract(10, 5)
    result2 = subtract(3, 7)
    print(result1)
    print(result2)