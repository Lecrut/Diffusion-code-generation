def string_length_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            print(f"Length of the string: {len(result)}")
        return result
    return wrapper

@string_length_decorator
def process_string(input_string):
    return input_string

if __name__ == '__main__':
    sample_string1 = "Hello, World!"
    sample_string2 = "Python Programming"
    processed_string1 = process_string(sample_string1)
    processed_string2 = process_string(sample_string2)