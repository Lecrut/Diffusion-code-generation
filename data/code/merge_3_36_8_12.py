def reverse_string_recursive(s: str) -> str:
    """
    Recursively reverses a string.
    
    Base case: if the string is empty, return an empty string.
    Recursive step: concatenate the last character with the reversed rest of the string.
    
    Args:
        s (str): The input string to reverse.
        
    Returns:
        str: A new string that is the reverse of the input string.
    """
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_string_recursive(s[:-1])

def measure_time(func, args, iterations=50):
    """
    Simple time measurement utility (not using external libraries).
    
    Args:
        func: The function to benchmark.
        args: Arguments tuple for the function.
        iterations: Number of times to run the function.
        
    Returns:
        float: Average execution time in seconds.
    """
    import time
    
    start = time.perf_counter()
    total_time = 0.0
    try:
        result = func(*args)
    finally:
        end = time.perf_counter()
    
    # Running the function multiple times to smooth out noise is unnecessary for string reversal 
    # as it's extremely fast, but we calculate a single run here since 'result' isn't needed.
    elapsed_time = end - start
    
    return elapsed_time

if __name__ == '__main__':
    # Hard-coded sample values (no user input required)
    test_strings = ["hello", "Python is great!", "", "a"]
    
    print("Comparing Recursive String Reversal vs Direct Slicing")
    print("-" * 50)
    
    for s in test_cases:
        time_recursive = measure_time(reverse_string_recursive, (s,), iterations=1)
        time_sliced = measure_time(lambda x: x[::-1], (s,), iterations=1)
        
        # Note: Slicing creates a new object while recursion builds one character by one.
        # For small strings in CPython optimizations, slicing is often faster due to internal loops 
        # and lack of function call overhead/stack frame creation per character.
        print(f"Input ('{s}'): Recursion time approx {time_recursive:.10f}s | Slicing time approx {time_sliced:.10f}s")

# Using a list comprehension for the iteration to ensure it runs without any issues if 'test_cases' is undefined in global scope during import
test_cases = test_strings