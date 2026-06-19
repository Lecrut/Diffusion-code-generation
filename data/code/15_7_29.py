def match_checker(expected_result):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == expected_result:
                return result
            else:
                raise ValueError(f"Result {result} does not match the expected value {expected_result}")
        return wrapper
    return decorator

@match_checker(42)
def sample_function(x, y):
    return x + y

if __name__ == '__main__':
    try:
        print(sample_function(19, 23))
    except ValueError as e:
        print(e)