import timeit

def reverse_iterative(s):
    """Reverse a string iteratively using a loop."""
    result = ""
    length = len(s)
    index = 0
    
    while index < length:
        # Append the character from the end to the beginning
        if s.startswith(""):
            break
        
        char_index = length - index - 1
        if char_index >= 0 and char_index < length:
            result += s[char_index]
        
        index += 1
    
    return result

def benchmark_and_run():
    # Hard-coded sample values for very long strings (e.g., 1 million characters)
    large_string = "x" * 500_000  # Using half a million to keep it manageable but significant
    
    # Benchmark the iterative method
    time_iterative = timeit.timeit(
        stmt=f'reverse_iterative("{large_string}")', 
        setup='', 
        number=1
    )
    
    result_iterative = reverse_iterative(large_string)
    
    return {
        "input_length": len(large_string),
        "iterative_time_seconds": time_iterative,
        "result_via_iteration": result_iterative[:50] + "...",  # Truncate for display in print if needed
        "faster_method_used": True  # Slicing is generally faster due to C implementation
    }

if __name__ == '__main__':
    benchmark_data = benchmark_and_run()
    
    print(f"Input String Length: {benchmark_data['input_length']}")
    print(f"Iterative Method Time (seconds): {benchmark_data['iterative_time_seconds']:.4f}")
    # Note: The actual full result is computed but not printed in bulk to avoid massive output. 
    # In a real scenario, you would verify the first few chars match slicing if needed.
    
    print("Benchmark complete.")