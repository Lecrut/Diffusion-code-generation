def string_length_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            print(f"Length of '{result}': {len(result)}")
        return result
    return wrapper

@string_length_decorator
def process_string(s):
    return s

if __name__ == '__main__':
    sample_values = ["Hello", "World!", "Python", "Decorator"]
    for value in sample_values:
        process_string(value)