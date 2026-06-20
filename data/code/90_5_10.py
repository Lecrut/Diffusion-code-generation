def or_test(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not any(cond(result) for cond in condition):
                raise ValueError(f"Function output {result} does not satisfy the 'or' condition")
            return result
        return wrapper
    return decorator

@or_test([lambda x: isinstance(x, int), lambda x: isinstance(x, float)])
def test_function():
    return 42.0

if __name__ == '__main__':
    print(test_function())