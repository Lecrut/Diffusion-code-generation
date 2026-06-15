def multiply(factor):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * factor
        return wrapper
    return decorator
@multiply(5)
def sample_function(x):
    return x
if __name__ == '__main__':
    input_value = 10
    output_value = sample_function(input_value)
    print(f"Input: {input_value}")
    print(f"Output: {output_value}")