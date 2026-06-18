def is_strictly_greater(func):
    """Decorator that ensures func(a, b) only executes if a > b."""
    def wrapper(*args, **kwargs):
        # Check condition: first argument strictly greater than second
        if len(args) >= 2 and args[0] <= args[1]:
            return None
        
        return func(*args, **kwargs)
    
    return wrapper

@is_strictly_greater
def add(a, b):
    """Simple function to test the decorator."""
    return a + b

if __name__ == '__main__':
    # Test case 1: First argument is strictly greater than second (should execute)
    result = add(5, 3)
    print(f"add(5, 3) returned: {result}")
    
    # Test case 2: First argument equals second (should not execute function logic)
    result = add(4, 4)
    print(f"add(4, 4) returned: {result}")
    
    # Test case 3: First argument is less than second (should not execute function logic)
    result = add(2, 5)
    print(f"add(2, 5) returned: {result}")