def is_strictly_greater(func):

    def wrapper(a, b):
        if a > b:
            return func(a, b)
        else:
            return None
    return wrapper

@is_strictly_greater
def multiply(a, b):
    return a * b
if __name__ == '__main__':
    result = multiply(5, 3)
    print(result)
    result = multiply(2, 4)
    print(result)