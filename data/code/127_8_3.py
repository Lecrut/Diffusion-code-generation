def mark_odd(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % 2 != 0:
            raise ValueError("Function returned an odd number, which is not allowed.")
        return result
    return wrapper
@mark_odd
def sample_function(x):
    return x
if __name__ == '__main__':
    print(sample_function(4))
    try:
        sample_function(5)
    except ValueError as e:
        print(f"Caught exception: {e}")
    try:
        sample_function(6)
    except ValueError as e:
        print(f"Caught exception: {e}")