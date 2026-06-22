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
def compute_sum(a, b):
    return a + b

if __name__ == '__main__':
    try:
        print(compute_sum(10, 5))
        print(compute_sum(-3, 7))
    except NegativeResultException as e:
        print(e)