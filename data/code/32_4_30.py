def string_length_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Length of the string: {len(result)}")
        return result
    return wrapper

@string_length_decorator
def process_string(input_string):
    return input_string.strip()

if __name__ == '__main__':
    sample_string = "  Hello, World!  "
    processed_string = process_string(sample_string)
    print(processed_string)