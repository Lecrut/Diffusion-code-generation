def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result[::-1]
        raise ValueError("The function did not return a string")
    return wrapper

@reverse_string_decorator
def get_message():
    return "Hello, World!"

if __name__ == '__main__':
    print(get_message())