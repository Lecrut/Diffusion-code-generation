def multiply_by_constant(factor):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) * factor
        return wrapper
    return decorator
@multiply_by_constant(5)
def double(x):
    return x * 2
@multiply_by_constant(10)
def triple(x):
    return x * 3
if __name__ == '__main__':
    result_double = double(4)
    result_triple = triple(5)
    print(f"double(4): {result_double}")
    print(f"triple(5): {result_triple}")