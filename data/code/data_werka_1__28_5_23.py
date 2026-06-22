def is_strictly_greater(func):

    def wrapper(a, b):
        if a > b:
            return func(a, b)
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