def repeat_n_times(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be an integer greater than 0")
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_n_times(5)
def print_message(message):
    print(message)

if __name__ == '__main__':
    print_message("Hello, world!")