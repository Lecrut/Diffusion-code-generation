import timeit

def reverse_iterative(s: str) -> str:
    """Reverses a string iteratively using a loop."""
    result = ""
    for char in s:
        result += char  # Inefficient but demonstrates iterative approach; optimized below if needed.
    
    return result[::-1]

# Optimized iterative reverse to avoid repeated concatenation overhead
def reverse_iterative_optimized(s: str) -> str:
    """Reverses a string iteratively using a loop with list append."""
    chars = []
    for char in s:
        chars.append(char)
    
    return "".join(reversed(chars))

# Benchmarking setup
if __name__ == '__main__':
    # Generate very long strings without user input or files
    sample_string_1k = "x" * 1000000
    
    times_iterative_optimized = timeit.timeit(
        stmt="reverse_iterative_optimized(sample_string_1k)", 
        setup="", 
        number=100
    ) / 100

    # Benchmarking slicing method (known to be fastest in CPython)
    times_slicing = timeit.timeit(
        stmt='"".join(reversed(sample_string_1k))', 
        setup="sample_string_1k", 
        number=100
    ) / 100

    # Select the faster result based on timing (though slicing is theoretically always better here)
    if times_iterative_optimized < times_slicing:
        final_result = reverse_iterative_optimized(sample_string_1k)
        method_used = "Iterative Optimized"
    else:
        final_result = "".join(reversed(sample_string_1k))
        method_used = "Slicing (Recommended)"

    print(f"Iterative time per run: {times_iterative_optimized:.6f}s")
    print(f"Slicing time per run: {times_slicing:.6f}s")
    print(f"Selected Method: {method_used}")