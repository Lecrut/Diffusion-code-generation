def repeat_n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_n_times(5)
def print_number(num):
    print(num)

if __name__ == '__main__':
    print_number(42)