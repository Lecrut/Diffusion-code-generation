def match_checker(expected_result):

    def wrapper(func):

        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if result == expected_result:
                return result
            else:
                raise ValueError(f'Result {result} does not match the expected value {expected_result}')
        return inner
    return wrapper

@match_checker(10)
def add(a, b):
    return a + b
if __name__ == '__main__':
    try:
        result = add(5, 5)
        print(result)
    except ValueError as e:
        print(e)
    try:
        result = add(3, 4)
        print(result)
    except ValueError as e:
        print(e)