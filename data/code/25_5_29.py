def check_zero_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            print("Zero result detected.")
        else:
            print(f"Non-zero result: {result}")
        return result
    return wrapper

@check_zero_result
def subtract(a, b):
    return a - b

if __name__ == '__main__':
    result1 = subtract(10, 10)
    print(result1)
    result2 = subtract(8, 3)
    print(result2)