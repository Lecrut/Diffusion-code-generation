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
def get_numbers(numbers):
    return numbers
@reverse
def get_string(text):
    return text
if __name__ == '__main__':
    print(get_numbers([1, 2, 3, 4]))
    print(get_string("hello"))