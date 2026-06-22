class NegativeValueException(Exception):
    def __init__(self, message):
        super().__init__(message)

def check_non_negative_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise NegativeValueException(f'Negative value detected: {result}')
        return result
    return wrapper

@check_non_negative_result
def calculate_product(a, b):
    return a * b

if __name__ == '__main__':
    try:
        print(calculate_product(4, 3))
        print(calculate_product(-1, 5))
    except NegativeValueException as e:
        print(e)