def subtract_constant(constant):
    def decorator(func):
        def wrapper(*args):
            result = 0
            for arg in args:
                result += arg - constant
            return result
        return wrapper
    return decorator
@subtract_constant(5)
def process_numbers(a, b, c):
    return a + b + c
if __name__ == '__main__':
    print(process_numbers(10, 20, 30))