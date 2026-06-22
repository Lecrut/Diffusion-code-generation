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
def calculate(a, b, operation):
    operations = {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b if b != 0 else float('inf')
    }
    return operations.get(operation, None)

if __name__ == '__main__':
    print(calculate(5, 3, 'add'))
    print(calculate(2, -2, 'subtract'))
    print(calculate(4, 2, 'multiply'))
    print(calculate(10, 0, 'divide'))