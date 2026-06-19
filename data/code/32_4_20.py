def string_length_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Length of the string: {len(result)}")
        return result
    return wrapper

@string_length_decorator
def get_string():
    return "Hello, World!"

if __name__ == '__main__':
    sample_string = get_string()
    print(sample_string)