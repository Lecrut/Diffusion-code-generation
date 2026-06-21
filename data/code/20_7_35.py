def check_eq(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, tuple) or len(result) != 2:
            raise ValueError('Function must return a tuple with two elements')
        first_value, second_value = result
        if first_value != second_value:
            raise AssertionError(f'Strict equality check failed: {first_value} != {second_value}')
        return (first_value, second_value)
    return wrapper

@check_eq
def compare_values(x, y):
    return (x, y)
if __name__ == '__main__':
    try:
        print(compare_values(10, 10))
        print(compare_values('test', 'test'))
        print(compare_values(3.5, 3.6))
    except (ValueError, AssertionError) as e:
        print(f'Caught an exception: {e}')