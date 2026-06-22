def is_strictly_greater(func):

    def wrapper(a, b):
        if a > b:
            return func(a, b)
        else:
            return None
    return wrapper

@is_strictly_greater
def add_numbers(x, y):
    return x + y
if __name__ == '__main__':
    result = add_numbers(10, 5)
    print(result)
    result = add_numbers(3, 7)
    print(result)