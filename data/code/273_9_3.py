import functools
def repeat_n_times(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
@repeat_n_times(3)
def say_hello(name):
    print(f"Hello, {name}")
if __name__ == '__main__':
    say_hello("World")