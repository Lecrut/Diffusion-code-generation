def product_calculator(constant_value):
    def decorator(func):
        def wrapper(*args):
            result = func(*args)
            return result * constant_value
        return wrapper
    return decorator
@product_calculator(constant_value=10)
def multiply_by_ten(x):
    return x
if __name__ == '__main__':
    sample_value = 5
    result = multiply_by_ten(sample_value)
    print(result)