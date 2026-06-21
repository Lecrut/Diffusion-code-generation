def reverse_string_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, str):
            raise ValueError("Function did not return a string")
        reversed_result = ''.join(reversed(result))
        return reversed_result
    return wrapper

@reverse_string_decorator
def get_greeting():
    return "Welcome to Alibaba Cloud!"

if __name__ == '__main__':
    print(get_greeting())