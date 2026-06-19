def check_not_equal_to_threshold(threshold):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == threshold:
                raise ValueError(f'Result {result} is equal to the threshold value.')
            return result
        return wrapper
    return decorator

@check_not_equal_to_threshold(0)
def difference(x, y):
    return x - y
if __name__ == '__main__':
    print(difference(5, 3))
    try:
        print(difference(4, 4))
    except ValueError as e:
        print(e)