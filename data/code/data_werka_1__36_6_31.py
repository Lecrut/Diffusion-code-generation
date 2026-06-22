def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[::-1]
    return wrapper

@reverse_string_decorator
def echo(message):
    return message

if __name__ == '__main__':
    sample_message = "Hello, World!"
    reversed_message = echo(sample_message)
    print(reversed_message)