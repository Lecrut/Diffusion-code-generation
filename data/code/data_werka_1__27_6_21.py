def check_not_equal_to_threshold(threshold):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == threshold:
                raise ValueError(f'Result is equal to the threshold value: {threshold}')
            return result
        return wrapper
    return decorator

@check_not_equal_to_threshold(0)
def difference(a, b):
    return a - b
if __name__ == '__main__':
    try:
        print(difference(5, 3))
        print(difference(4, 4))
    except ValueError as e:
        print(e)