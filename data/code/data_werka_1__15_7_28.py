def match_checker(expected_value):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == expected_value:
                return True
            else:
                return False
        return wrapper
    return decorator

@match_checker(42)
def sample_function():
    return 42
if __name__ == '__main__':
    print(sample_function())