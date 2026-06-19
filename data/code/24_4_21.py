class NegativeResultError(Exception):
    def __init__(self, message):
        super().__init__(message)

def check_negative_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise NegativeResultError(f'Negative result detected: {result}')
        return result
    return wrapper

@check_negative_result
def sample_function(x, y):
    return x + y

if __name__ == '__main__':
    try:
        print(sample_function(5, 3))
        print(sample_function(-1, 2))
    except NegativeResultError as e:
        print(e)