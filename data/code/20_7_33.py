def check_eq(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not result:
            raise ValueError("Function did not return True")
        return result
    return wrapper

@check_eq
def add(a, b):
    return a + b == 3

@check_eq
def multiply(a, b):
    return a * b == 6

if __name__ == '__main__':
    print(add(1, 2))
    print(multiply(2, 3))