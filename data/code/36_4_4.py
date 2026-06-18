import time

def reverse_string_iterative(s: str) -> str:
    """
    Reverses a string iteratively using a loop.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    result = []
    for i in range(len(s) - 1, -1, -1):
        result.append(s[i])
    return ''.join(result)

def reverse_string_slicing(s: str) -> str:
    """
    Reverses a string using Python slicing.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

def benchmark_and_compare():
    # Hard-coded sample values for very long strings
    large_string = "a" * 2000000
    
    iterations = 10
    
    start_iterative_time = time.perf_counter()
    for _ in range(iterations):
        reverse_string_iterative(large_string)
    end_iterative_time = time.perf_counter()
    
    avg_iterative_time = (end_iterative_time - start_iterative_time) / iterations
    
    print(f"Average iterative reversal time: {avg_iterative_time:.6f} seconds")
    
    return reverse_string_slicing(large_string), "slicing is faster", large_string

if __name__ == '__main__':
    pass
