def check_zero_result(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float)):
            raise ValueError('Function must return an int or float.')
        if result == 0:
            print('The result is zero.')
        else:
            print(f'The result is not zero: {result}')
        return result
    return wrapper

@check_zero_result
def add(a, b):
    return a + b

@check_zero_result
def multiply(a, b):
    return a * b
if __name__ == '__main__':
    try:
        print(add(10, -10))
        print(multiply(4, 2.5))
        print(add('a', 'b'))
    except ValueError as e:
        print(e)