class NegativeValueException(Exception):
    def __init__(self, message):
        super().__init__(message)

def check_non_negative_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise NegativeValueException(f'Function {func.__name__} returned a negative value: {result}')
        return result
    return wrapper

@check_non_negative_result
def calculate_sum(a, b):
    return a + b

if __name__ == '__main__':
    try:
        print(calculate_sum(4, 3))
        print(calculate_sum(-1, 5))
    except NegativeValueException as e:
        print(e)