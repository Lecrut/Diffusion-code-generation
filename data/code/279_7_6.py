def range_iterator(start, stop):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(start, stop):
                result = func(i)
                yield result
        return wrapper
    return decorator
@range_iterator(1, 5)
def multiply(n):
    return n * 2
@range_iterator(0, 3)
def add_one(n):
    return n + 1
if __name__ == '__main__':
    print("Testing multiply function:")
    for val in multiply():
        print(val)
    print("\nTesting add_one function:")
    for val in add_one():
        print(val)