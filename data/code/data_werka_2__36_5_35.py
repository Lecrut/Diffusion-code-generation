def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[::-1]
    return wrapper

@reverse_string_decorator
def greet(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    print(greet("Alice"))