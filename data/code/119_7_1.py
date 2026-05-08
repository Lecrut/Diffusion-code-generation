def reverse_args(func):
    def wrapper(*args):
        reversed_args = tuple(reversed(args))
        return func(*reversed_args)
    return wrapper
@reverse_args
def my_function(a, b, c):
    return a, b, c
if __name__ == '__main__':
    result = my_function(1, 2, 3)
    print(result)