def check_not_equal(threshold):

    def decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == threshold:
                raise ValueError(f'Result is equal to the threshold value: {threshold}')
            return result
        return wrapper
    return decorator

@check_not_equal(0)
def difference(x, y):
    return x - y
if __name__ == '__main__':
    try:
        print(difference(10, 5))
        print(difference(3, 3))
    except ValueError as e:
        print(e)