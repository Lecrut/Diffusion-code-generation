def string_length_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            print(f"Length of the string: {len(result)}")
        return result
    return wrapper

@string_length_decorator
def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    print(greet(sample_string))