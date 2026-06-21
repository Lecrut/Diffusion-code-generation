def check_zero_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            print("Zero encountered!")
        else:
            print(f"Result is {result}, not zero.")
        return result
    return wrapper

@check_zero_result
def subtract(a, b):
    return a - b

if __name__ == '__main__':
    subtract(10, 5)
    subtract(7, 7)