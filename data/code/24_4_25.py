class NegativeResultException(Exception):
    def __init__(self, message):
        super().__init__(message)

def check_negative_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise NegativeResultException(f'Negative result detected: {result}')
        return result
    return wrapper

@check_negative_result
def compute_square_root(x):
    import math
    return math.sqrt(x)

if __name__ == '__main__':
    try:
        print(compute_square_root(16))
        print(compute_square_root(-4))
    except NegativeResultException as e:
        print(e)