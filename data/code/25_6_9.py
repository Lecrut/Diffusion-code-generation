def check_result_zero(func):
    """
    A decorator that wraps a function to automatically add functionality 
    checking if its result is zero upon execution, printing it out.
    
    Args:
        func (callable): The original function to wrap.
        
    Returns:
        callable: The wrapped function with the added check logic.
    """
    def wrapper(*args, **kwargs):
        # Call the original function and store its result
        result = func(*args, **kwargs)
        # Check if the result is zero (using == for exact integer/float comparison in this context)
        if result == 0:
            print("The result of the wrapped function is zero.")
        return result
    return wrapper

# Sample block execution without user input or external dependencies
if __name__ == '__main__':
    # Define a sample function that returns 0
    def square_and_subtract(x, y):
        """Calculates x*x - y"""
        return (x ** 2) - (y * 1.5)

    # Another sample returning non-zero for variety
    def add_numbers(a, b):
        return a + b
    
    # Testing the zero-checking decorator on square_and_subtract(3, 9/4 -> 8*0.75=6? No wait: 3^2 - (1.5)*9 = 9 - 13.5 != 0)
    # Let's fix sample to ensure one returns zero for demonstration clarity if needed, 
    # but the task doesn't require guaranteed zeros in samples, just that it works when result IS zero.
    
    print("Testing function returning non-zero:")
    add_numbers(2, 3)

    # Constructing a specific case where square_and_subtract returns exactly 0: x=1.5, y=(9/4)*x? 
    # Let's simply use variables that make it zero explicitly for the check demo if we wanted, 
    # but let's just run the existing one to show non-zero behavior.
    
    result_sq = square_and_subtract(3, 6) # 9 - 9 = 0
    
    print("Testing function returning zero:")
    @check_result_zero
    def test_zero_func():
        return 42 + (-42)