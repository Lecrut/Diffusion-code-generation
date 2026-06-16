def reverse(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (list, tuple)):
            return reversed(result)
        else:
            return result
    return wrapper
import functools
@reverse
def get_numbers(data):
    return list(data)
@reverse
def get_string(text):
    return text[::-1]
if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    reversed_numbers = get_numbers(numbers)
    print(f"Reversed numbers: {reversed_numbers}")
    text = "hello world"
    reversed_text = get_string(text)
    print(f"Reversed string: {reversed_text}")