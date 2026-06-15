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
    print(f"Executing greet for {name}")
    return f"Hello, {name}"
if __name__ == '__main__':
    print("--- Testing greet function ---")
    output = greet("World")
    print(f"Final result: {output}")