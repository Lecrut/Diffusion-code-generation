def check_truth(condition):

    def decorator(func):

        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                return None
        return wrapper
    return decorator

@check_truth(True)
def add(a, b):
    return a + b

@check_truth(False)
def multiply(a, b):
    return a * b
if __name__ == '__main__':
    result_add = add(3, 4)
    print(result_add)
    result_multiply = multiply(3, 4)
    print(result_multiply)