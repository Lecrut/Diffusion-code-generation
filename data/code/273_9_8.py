def repeat_n_times(n):
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
    print_message("Hello, World!")