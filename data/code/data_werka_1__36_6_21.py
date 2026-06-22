def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[::-1]
    return wrapper

@reverse_string_decorator
def process_string(s):
    return s

if __name__ == '__main__':
    sample_value = "Hello, World!"
    print(process_string(sample_value))