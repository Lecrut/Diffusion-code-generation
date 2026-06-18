def is_strictly_greater(func):
    """Decorator that ensures func executes only if first arg > second arg."""
    def wrapper(first_arg, second_arg, *args, **kwargs):
        return func(first_arg, second_arg, *args, **kwargs) if first_arg > second_arg else None
    return wrapper

@is_strictly_greater
def add_numbers(a: int, b: int, c: float = 0.0) -> float:
    """Adds three numbers."""
    return a + b + c

if __name__ == '__main__':
    # Test case where first argument is strictly greater than the second
    result1 = add_numbers(5, 3, 2.5)
    
    # Test case where condition fails (should not execute function body logic effectively for return value in this context)
    # Note: The decorator returns None if condition isn't met, preventing execution of func's internal logic? 
    # Actually, the wrapper calls func only if condition is true. If false, it returns None immediately without calling func.
    
    print(f"Result when 5 > 3 (should execute): {result1}")
    
    result2 = add_numbers(4, 6, 0)
    print(f"Result when 4 <= 6 (condition failed, function not called): {result2}")