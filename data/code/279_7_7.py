def range_iterator(start, stop):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(start, stop):
                result = func(i)
                yield result
        return wrapper
    return decorator
@range_iterator(0, 5)
def multiply(x):
    return x * 2
@range_iterator(1, 4)
def add_one(x):
    return x + 1
if __name__ == '__main__':
    print("Testing multiply function:")
    for value in multiply():
        print(value)
    print("\nTesting add_one function:")
    for value in add_one():
        print(value)