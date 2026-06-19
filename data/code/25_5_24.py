def check_zero_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            print("The result is zero.")
        return result
    return wrapper

@check_zero_result
def add(a, b):
    return a + b

if __name__ == '__main__':
    result1 = add(5, -5)
    print(result1)
    result2 = add(3, 7)
    print(result2)