def conditional_execution(*conditions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if all(conditions):
                return func(*args, **kwargs)
            else:
                return None
        return wrapper
    return decorator
@conditional_execution(True, "A", 10)
def my_function(x, y, z):
    return f"Executed with x={x}, y={y}, z={z}"
@conditional_execution(False, "B", 20)
def another_function(x, y, z):
    return f"Executed with x={x}, y={y}, z={z}"
if __name__ == '__main__':
    print(my_function(1, 2, 3))
    print(another_function(4, 5, 6))