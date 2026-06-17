def safe_divide(func):
    def wrapper(*args):
        try:
            result = func(*args)
            return result
        except ZeroDivisionError:
            return "Error: Cannot divide by zero"
    return wrapper
@safe_divide
def perform_division(a, b):
    return a / b
if __name__ == '__main__':
    print(perform_division(10, 2))
    print(perform_division(10, 0))