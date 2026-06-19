def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[::-1]
    return wrapper

@reverse_string_decorator
def get_sample_string():
    return "Hello, World!"

if __name__ == '__main__':
    print(get_sample_string())