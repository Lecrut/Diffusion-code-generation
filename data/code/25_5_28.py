def check_zero_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            print("Zero Result Detected")
        else:
            print(f"Non-Zero Result: {result}")
        return result
    return wrapper

@check_zero_result
def subtract(a, b):
    return a - b

if __name__ == '__main__':
    subtract(10, 5)
    subtract(7, 7)