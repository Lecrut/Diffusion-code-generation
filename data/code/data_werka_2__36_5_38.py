def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result[::-1]
        raise ValueError("The function must return a string")
    return wrapper

@reverse_string_decorator
def sample_function(input_string):
    return input_string

if __name__ == '__main__':
    print(sample_function("Hello, World!"))