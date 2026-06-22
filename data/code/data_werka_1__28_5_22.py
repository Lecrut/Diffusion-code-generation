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
    result1 = add_numbers(5, 3)
    result2 = add_numbers(2, 4)
    print(result1)
    print(result2)