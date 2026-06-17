def repeat_n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
@repeat_n_times(3)
def greet(name):
    print(f"Hello, {name}")
if __name__ == '__main__':
    greet("Alice")