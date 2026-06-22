def check_zero_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            print("The result is zero.")
        else:
            print(f"The result is not zero: {result}")
        return result
    return wrapper

@check_zero_result
def add(a, b):
    return a + b

@check_zero_result
def multiply(a, b):
    return a * b

if __name__ == '__main__':
    add(5, 3)
    add(2, -2)
    multiply(4, 0)
    multiply(6, 7)