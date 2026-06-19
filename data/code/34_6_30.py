def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return ' '.join(word.capitalize() for word in result.split())
    return wrapper

@capitalize_decorator
def sample_function(input_string):
    return input_string

if __name__ == '__main__':
    sample_input = "hello world from alibaba cloud"
    print(sample_function(sample_input))