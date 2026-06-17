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
def add(a, b):
    return a + b
@subtract_constant(10)
def multiply(a, b):
    return a * b
if __name__ == '__main__':
    result1 = add(3, 4)
    print(f"add(3, 4) with constant 5: {result1}")
    result2 = multiply(2, 6)
    print(f"multiply(2, 6) with constant 10: {result2}")