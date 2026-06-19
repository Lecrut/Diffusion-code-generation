def string_length_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        length = len(result)
        print(f"Length of the string: {length}")
        return result
    return wrapper

@string_length_decorator
def get_string():
    return "Hello, World!"

if __name__ == '__main__':
    sample_string = get_string()
    print(sample_string)