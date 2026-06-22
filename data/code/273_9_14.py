def repeat_n_times(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = [func(*args, **kwargs) for _ in range(n)]
            return results
        return wrapper
    return decorator

@repeat_n_times(5)
def generate_number():
    return 42

if __name__ == '__main__':
    numbers = generate_number()
    print(numbers)