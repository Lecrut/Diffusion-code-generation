def string_length_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Length of '{result}': {len(result)}")
        return result
    return wrapper

@string_length_decorator
def echo_string(s):
    return s

if __name__ == '__main__':
    sample_string1 = "Hello, World!"
    sample_string2 = "Python Programming"
    echo_string(sample_string1)
    echo_string(sample_string2)