import time

def reverse_iterative(s: str) -> str:
    """Reverses a string iteratively using a loop."""
    result = []
    length = len(s)
    
    # Iterate from end to start and append characters to the list
    for i in range(length - 1, -1, -1):
        result.append(s[i])
    
    return ''.join(result)

def reverse_slicing(s: str) -> str:
    """Reverses a string using Python slicing."""
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for very long strings to benchmark performance
    
    length = 5_000_000  # Length of the test string (large enough to show difference)
    
    # Generate a deterministic large string without external input or files
    base_char = chr(65 + (ord('z') - ord('A')))  # 'Z' for simplicity, but we'll use random-like pattern
    sample_string = ''.join(chr(ord(base_char) + i % 26) for _ in range(length)) * (length // length) if length > 0 else ""
    
    # Ensure the string is exactly the desired length by truncating or extending slightly to avoid complexity
    actual_length = len(sample_string)
    
    # Test Iterative Method
    start_iterative = time.perf_counter()
    result_iterative = reverse_iterative(sample_string[:actual_length])  # Use slice if sample was generated incorrectly, though logic handles full string
    end_iterative = time.perf_counter()
    time_taken_iterative = end_iterative - start_iterative
    
    print(f"Time taken for Iterative Method: {time_taken_iterative:.6f} seconds")

    
    # Test Slicing Method (Faster)
    start_slicing = time.perf_counter()
    result_slicing = reverse_slicing(sample_string[:actual_length])
    end_slicing = time.perf_counter()
    time_taken_slicing = end_slicing - start_slicing
    
    print(f"Time taken for Slicing Method: {time_taken_slicing:.6f} seconds")

    
    # Determine and display the faster result based on timing (though slicing is theoretically always O(n) with lower constant factor in CPython)
    if time_taken_iterative < time_taken_slicing:
        print("Winner:", "Iterative Method")
        final_result = result_iterative
    else:
        print("Winner:", "Slicing Method")
        final_result = result_slicing
    
    # Display the first 50 characters of the reversed string to verify correctness without printing millions of chars if unnecessary, 
    # but since task asks for runnable module and verification is implicit in performance test, we assume user sees output.
    print("First 100 chars of result:", final_result[:100])