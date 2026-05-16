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
    print("Testing with an even number (should pass):")
    try:
        result_even = sample_function(4)
        print(f"Result: {result_even}")
    except ValueError as e:
        print(f"Caught exception: {e}")
    print("\nTesting with an odd number (should raise exception):")
    try:
        result_odd = sample_function(5)
        print(f"Result: {result_odd}")
    except ValueError as e:
        print(f"Caught exception: {e}")