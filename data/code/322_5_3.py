def safe_divide(func):
    def wrapper(*args):
        try:
            result = func(*args)
            return result
        except ZeroDivisionError:
            return "Error: Cannot divide by zero"
    return wrapper
@safe_divide
def simple_divide(a, b):
    return a / b
if __name__ == '__main__':
    print(simple_divide(10, 2))
    print(simple_divide(10, 0))