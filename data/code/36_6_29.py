def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[::-1]
    return wrapper

@reverse_string_decorator
def sample_function(input_string):
    return input_string

if __name__ == '__main__':
    sample_input = "Hello, World!"
    print(sample_function(sample_input))