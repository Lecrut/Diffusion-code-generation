def reverse_args(func):
    def wrapper(*args):
        reversed_args = list(args)
        reversed_args.reverse()
        return func(*reversed_args)
    return wrapper
add_reversed = reverse_args
def reverse_args_decorator(func):
    def wrapper(*args):
        reversed_args = list(args)
        reversed_args.reverse()
        return func(*reversed_args)
    return wrapper
@reverse_args_decorator
def func_to_reverse(a, b, c):
    return a, b, c
if __name__ == '__main__':
    original_args = (1, 2, 3)
    result = func_to_reverse(*original_args)
    print(result)