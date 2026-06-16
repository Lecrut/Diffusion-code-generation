def range_iterator(start, stop):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(start, stop):
                result = func(i)
                yield result
        return wrapper
    return decorator
@range_iterator(1, 5)
def square(n):
    return n * n
@range_iterator(2, 6)
def cube(n):
    return n ** 3
if __name__ == '__main__':
    print("Square results:")
    for item in square():
        print(item)
    print("\nCube results:")
    for item in cube():
        print(item)