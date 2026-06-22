def check_zero_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if is_zero(result):
            print("The result is zero.")
        else:
            print(f"The result is not zero: {result}")
        return result
    return wrapper

def is_zero(value):
    return value == 0

@check_zero_result
def add(a, b):
    return a + b

@check_zero_result
def multiply(a, b):
    return a * b

if __name__ == '__main__':
    add(10, -10)
    add(4, 5)
    multiply(6, 0)
    multiply(3, 7)