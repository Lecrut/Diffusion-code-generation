def capitalize_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return ' '.join(word.capitalize() for word in result.split())
    return wrapper

@capitalize_decorator
def sample_function(input_string):
    return input_string

if __name__ == '__main__':
    sample_text = "hello world this is a test"
    capitalized_text = sample_function(sample_text)
    print(capitalized_text)