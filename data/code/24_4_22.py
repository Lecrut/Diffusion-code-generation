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
def compute_difference(x, y):
    return x - y

if __name__ == '__main__':
    try:
        print(compute_difference(15, 10))
        print(compute_difference(5, 20))
    except NegativeResultException as e:
        print(e)