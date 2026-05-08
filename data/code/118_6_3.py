def product_calculator(constant_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * constant_value
        return wrapper
    return decorator
@product_calculator(constant_value=5)
def multiply_by_five(x):
    return x
if __name__ == '__main__':
    sample_value = 10
    result = multiply_by_five(sample_value)
    print(result)