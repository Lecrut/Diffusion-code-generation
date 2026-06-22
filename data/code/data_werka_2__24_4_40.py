class NonPositiveResultException(Exception):
    def __init__(self, message):
        super().__init__(message)

def ensure_non_negative(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise NonPositiveResultException(f'Function {func.__name__} returned a non-positive value: {result}')
        return result
    return wrapper

@ensure_non_negative
def compute_quotient(a, b):
    return a / b

if __name__ == '__main__':
    try:
        print(compute_quotient(10, 2))
        print(compute_quotient(5, -1))
    except NonPositiveResultException as e:
        print(e)