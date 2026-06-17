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
def subtract_five(a, b):
    return a + b
@subtract_constant(10)
def subtract_ten(x):
    return x * 2
if __name__ == '__main__':
    result1 = subtract_five(3, 4)
    print(f"Result of subtract_five(3, 4): {result1}")
    result2 = subtract_ten(5)
    print(f"Result of subtract_ten(5): {result2}")