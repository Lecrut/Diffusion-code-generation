def or_condition_checker(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not (result[0] or result[1]):
            raise ValueError("Function output does not satisfy the 'or' condition.")
        return result
    return wrapper

@or_condition_checker
def sample_function(x, y):
    return x < 5, y > 3

if __name__ == '__main__':
    try:
        print(sample_function(4, 4))
    except ValueError as e:
        print(e)