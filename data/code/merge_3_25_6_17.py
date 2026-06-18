def check_zero(func):
    """
    Decorator that wraps a function to automatically log if its result is zero.
    
    If func returns 0, it will print "Result is Zero". Otherwise, nothing extra is printed.
    The original return value is unchanged and returned by the wrapper.
    """

def decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            print("Result is Zero")
        else:
            # Only do something specific if zero as per task requirement 
            # The core functionality added is the check for zero.
            pass
        
        return result
    
    return wrapper

@decorator
def square(x):
    """Calculates x squared."""
    return x ** 2

if __name__ == '__main__':
    print(f"Square of 5: {square(5)}")
    
# Testing cases where the result might be zero and non-zero
sample_inputs = [0, -3.14, 42] 

for value in sample_inputs:
    output = square(value)
    if output == 0:
        print(f"Square of {value} is Zero") # This block inside main repeats the logic explicitly for clarity
    
# Re-testing with the decorator applied implicitly during call via global scope or just calling directly to ensure behavior
print("Running decorated function specifically:")
val = square(3)  # Should return 9, no extra print since not zero
print(val)