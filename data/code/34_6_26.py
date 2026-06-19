def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return ' '.join(word.capitalize() for word in result.split())
    return wrapper

@capitalize_decorator
def format_string(input_string):
    return input_string

if __name__ == '__main__':
    sample_input = "hello world this is a test"
    capitalized_output = format_string(sample_input)
    print(capitalized_output)