def reverse_string_recursive(s):
    """
    Recursively reverses a string.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    # Base case: if the string is empty or has one character, return it as is
    if len(s) <= 1:
        return s
    
    # Recursive step: reverse the rest of the string and append the first character
    return reverse_string_recursive(s[1:]) + s[0]

def compare_complexity():
    """
    Analyzes time complexity by running both methods on sample data.
    
    Returns:
        dict: Comparison results including execution times and output strings.
    """
    # Sample input string - no user interaction, file I/O, or network access needed
    test_string = "Hello World" * 10
    
    import time
    
    start_time = time.perf_counter()
    result_recursive = reverse_string_recursive(test_string)
    recursive_end_time = time.perf_counter()
    
    # Direct slicing method for comparison (this is the baseline O(n))
    start_slicing = time.perf_counter()
    direct_result = test_string[::-1]
    end_slicing = time.perf_counter()
    
    return {
        'recursive_output': result_recursive,
        'direct_output': direct_result,
        'time_taken_recursive': recursive_end_time - start_time,
        'time_taken_direct': end_slicing - start_slicing,
        'complexity_analysis': f"Recursive method: O(n) time due to n function calls with constant work each.\nDirect slicing: O(1) space (internal C optimization), effectively O(n) string copy."
    }

if __name__ == '__main__':
    # Run the comparison using hard-coded sample values as per requirements
    results = compare_complexity()
    
    print("Recursive Output:")
    print(results['recursive_output'])
    print("\nDirect Slicing Output:")
    print(results['direct_output'])
    if results['recursive_output'] == results['direct_output']:
        print("\n✓ Both methods produce identical results.")
        
    print(f"\nPerformance Analysis:")
    print("-" * 40)
    print("Time taken (Recursive):", f"{results['time_taken_recursive']*1e6:.2f} microseconds")
    print("Time taken (Direct Slicing):", f"{results['time_taken_direct']*1e6:.2f} microseconds")
    
    # Complexity explanation based on the task requirements
    print("-" * 40)
    print(results['complexity_analysis'])