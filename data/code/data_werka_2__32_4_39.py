def string_length_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            print(f"Length of the string: {len(result)}")
        else:
            raise ValueError("The function did not return a string.")
        return result
    return wrapper

@string_length_decorator
def get_greeting():
    return "Hello, World!"

if __name__ == '__main__':
    greeting = get_greeting()
    print(greeting)