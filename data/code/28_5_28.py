def is_strictly_greater(func):

    def wrapper(a, b):
        if a > b:
            return func(a, b)
        else:
            return None
    return wrapper

@is_strictly_greater
def add(a, b):
    return a + b
if __name__ == '__main__':
    result = add(10, 5)
    print(result)
    result = add(3, 7)
    print(result)