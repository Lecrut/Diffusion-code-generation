def match_checker(expected_value):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == expected_value:
                return result
            else:
                raise ValueError(f'Result {result} does not match the expected value {expected_value}')
        return wrapper
    return decorator

@match_checker(10)
def add_numbers(a, b):
    return a + b
if __name__ == '__main__':
    try:
        result = add_numbers(5, 5)
        print(result)
    except ValueError as e:
        print(e)
    try:
        result = add_numbers(3, 4)
        print(result)
    except ValueError as e:
        print(e)