def or_test(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not any(result == c for c in condition):
                raise ValueError(f"Function output {result} does not satisfy the 'or' condition: {condition}")
            return result
        return wrapper
    return decorator

@or_test([True, False])
def test_function():
    return True

if __name__ == '__main__':
    print(test_function())