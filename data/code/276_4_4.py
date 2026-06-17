def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@repeat(3)
def greet(name):
    print(f"Greeting for {name}")
    return f"Hello, {name}"
if __name__ == '__main__':
    print("Testing the decorated function:")
    final_result = greet("World")
    print("\nFinal result after 3 repetitions:")
    print(final_result)