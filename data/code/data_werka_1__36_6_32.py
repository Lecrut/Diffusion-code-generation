def reverse_string_decorator(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result[::-1]
        return result
    return wrapper

@reverse_string_decorator
def sample_function(input_str):
    return input_str
if __name__ == '__main__':
    print(sample_function('Hello, World!'))
    print(sample_function('Python'))
    print(sample_function(12345))