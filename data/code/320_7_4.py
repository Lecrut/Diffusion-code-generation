def subtract_constant(constant):
    def decorator(func):
        def wrapper(*args):
            new_args = []
            for arg in args:
                if isinstance(arg, (int, float)):
                    new_args.append(arg - constant)
                else:
                    new_args.append(arg)
            return func(*new_args)
        return wrapper
    return decorator
@subtract_constant(5)
def process_numbers(a, b):
    return a + b
if __name__ == '__main__':
    result = process_numbers(10, 20)
    print(result)