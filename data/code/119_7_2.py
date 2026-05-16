def reverse_args(func):
    def wrapper(*args):
        new_args = list(args)
        new_args.reverse()
        return func(*new_args)
    return wrapper
add_reversed = reverse_args
def reverse_args_decorator(func):
    def wrapper(*args):
        reversed_args = tuple(reversed(list(args)))
        return func(*reversed_args)
    return wrapper
@reverse_args_decorator
def example_function(a, b, c):
    return a, b, c
if __name__ == '__main__':
    print(example_function(1, 2, 3))