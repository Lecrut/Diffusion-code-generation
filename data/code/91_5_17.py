def negate_decorator(negate):
    if not isinstance(negate, bool):
        raise ValueError("The 'negate' parameter must be a boolean.")
    
    def wrapper(func):
        def inner(*args, **kwargs):
            return not func(*args, **kwargs)
        return inner
    
    return wrapper

@negate_decorator(True)
def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    print(is_even(4))
    print(is_even(5))