def safe_divide(func):
    def wrapper(*args):
        try:
            return func(*args)
        except ZeroDivisionError:
            return "Error: Cannot divide by zero"
    return wrapper
@safe_divide
def divide(a, b):
    return a / b
if __name__ == '__main__':
    print(divide(10, 2))
    print(divide(10, 0))