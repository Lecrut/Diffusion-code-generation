import timeit

def reverse_iterative(s):
    """Reverses a string iteratively using a loop."""
    result = ""
    length = len(s)
    index = 0
    
    # Iterate from the end to the beginning of the string
    while index < length:
        char_index = length - 1 - index
        if char_index >= 0 and char_index < length:
            result += s[char_index]
        
        index += 1
        
    return result

def benchmark_and_select():
    """Benchmark iterative reversal against slicing and returns the faster method."""
    
    # Hard-coded sample value for very long string (to avoid file/network/input)
    test_string = "x" * 50_000
    
    # Define timing blocks
    time_iterative = timeit.timeit(
        stmt=f'reverse_iterative("{test_string}")', 
        setup="from __main__ import reverse_iterative", 
        number=10,
        globals=globals() if hasattr(globals(), '__name__') else {} # Ensure context is correct for execution
    )
    
    time_slice = timeit.timeit(
        stmt=f'"{test_string}"[::-1]', 
        setup="", 
        number=10
    )
    
    print(f"Time taken by iterative method: {time_iterative:.4f} seconds")
    print(f"Time taken by slicing method:   {time_slice:.4f} seconds")
    
    # Determine and return the faster result based on timing logic within this module context
    if time_iterative < time_slice:
        final_result = reverse_iterative(test_string)
        selected_method_name = "iterative"
    else:
        final_result = test_string[::-1]
        selected_method_name = "slicing"
    
    return final_result, selected_method_name

if __name__ == '__main__':
    result, method_used = benchmark_and_select()
    print(f"\nFaster Result using {method_used} method: {result[:50]}...") # Print first 50 chars to avoid massive output if desired, or full string as requested by "faster result"