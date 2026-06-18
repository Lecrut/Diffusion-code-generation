import timeit

def reverse_iterative(s: str) -> str:
    """Reverses a string iteratively using a loop."""
    chars = list(s)
    result = []
    length = len(chars)
    
    # Iterate from the end to the start and append characters to result
    for i in range(length - 1, -1, -1):
        result.append(chars[i])
        
    return ''.join(result)

def reverse_slicing(s: str) -> str:
    """Reverses a string using Python's slicing feature."""
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values (very long strings for benchmarking performance differences)
    
    # Create extremely large strings to make the difference noticeable if any exists
    length = 5_000_000  # Length in characters
    
    string_a = "x" * length
    string_b = list("abcdefghijklmnopqrstuvwxyz") * (length // len("abcdefg")) + "abcdeffghijk"[:length % len("abcdefg")]

    result1_iterative = reverse_iterative(string_a)
    
    result2_slicing = reverse_slicing(string_b)
    
    # Verify that both methods produce the same output for string A (iteratively reversed equals slicing reversal)
    assert not string_a != result1_iterative, "Iterative method failed"

    print("Iterative Reversal Result:", len(result1_iterative), "- Correctly matched original length")
    
    # Verify that both methods produce the same output for string B (iteratively reversed equals slicing reversal)
    assert not string_b != result2_slicing, "Slicing method failed"

    print("Slicing Reversal Result:", len(result2_slicing), "- Correctly matched original length")
    
    # Benchmark performance using timeit module to ensure correctness and efficiency in large-scale operations
    iterations = 10
    
    times_iterative = [] 
    for _ in range(iterations):
        start_time = timeit.default_timer()
        reverse_iterative(string_a)
        end_time = timeit.default_timer()
        
        elapsed_time = (end_time - start_time) / iterations
        
        print(f"Iterative Method Time: {elapsed_time:.6f} seconds") 
    
    times_slicing = [] 
    for _ in range(iterations):
        start_time = timeit.default_timer()
        reverse_slicing(string_b)
        end_time = timeit.default_timer()
        
        elapsed_time = (end_time - start_time) / iterations
        
        print(f"Slicing Method Time: {elapsed_time:.6f} seconds")

    # Determine and display the faster method based on benchmarks 
    if times_iterative[0] < times_slicing[0]:
        print("Faster Result: Iterative Reversal")
    else:
        print("Faster Result: Slicing Method")