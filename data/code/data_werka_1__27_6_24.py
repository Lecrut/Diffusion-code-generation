def not_equal_to_threshold(threshold):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == threshold:
                raise ValueError(f'Result is equal to the threshold value: {threshold}')
            return result
        return wrapper
    return decorator

@not_equal_to_threshold(0)
def check_difference(a, b):
    return a - b
if __name__ == '__main__':
    try:
        print(check_difference(5, 3))
        print(check_difference(4, 4))
    except ValueError as e:
        print(e)