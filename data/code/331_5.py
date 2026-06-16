def lowercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.lower()
    return wrapper
@lowercase_decorator
def get_greeting(name):
    return "Hello, World!"
if __name__ == '__main__':
    original_result = get_greeting("Alice")
    print(f"Original result: {original_result}")