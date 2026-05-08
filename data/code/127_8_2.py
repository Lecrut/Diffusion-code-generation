def mark_odd(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result % 2 != 0:
            raise ValueError("Function returned an odd number. Only even results are allowed.")
        return result
    return wrapper
@mark_odd
def sample_function(x):
    return x
if __name__ == '__main__':
    try:
        print(f"Testing with even number: {sample_function(4)}")
        print(f"Testing with odd number: {sample_function(5)}")
    except ValueError as e:
        print(f"Caught exception: {e}")