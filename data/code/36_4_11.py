import timeit

def reverse_iterative(s: str) -> str:
    """Reverse a string using an iterative loop."""
    result = []
    i, length = 0, len(s)
    
    # Pre-allocate the list (optional optimization for very long strings)
    while i < length:
        result.append(s[length - 1 - i])
        i += 1
    
    return "".join(result)

def benchmark_and_select():
    """Benchmark iterative vs slicing methods and return the faster one."""
    
    # Generate a very large string (approx 20 million chars to make difference visible)
    test_string = "a" * 20_000_000
    
    # Measure performance of slicing method using timeit
    # Slicing creates a copy, so we measure it directly as usually intended for 'reverse' in Python
    slice_time = timeit.timeit(
        stmt=f"'{test_string}'[::-1]", 
        setup="", 
        number=3  # Run a few times to reduce noise variance without waiting too long on local machines
    ) / (len(test_string) * 0.85)  # Normalize roughly per char, adjusted for list overhead
    
    # Measure performance of iterative method using timeit
    iter_time = timeit.timeit(
        stmt=f"reverse_iterative('{test_string}')", 
        setup="", 
        number=3
    ) / (len(test_string))  # Simple approximation to compare work done per character
    
    return slice_test, iter_test

def reverse_with_benchmark():
    """Main benchmarking logic wrapped as requested."""
    
    test_data = "a" * 20_000_000
    iterations = 3 

    time_slice_total = sum(timeit.timeit(
        stmt=f"'{test_data}'[::-1]", 
        setup="", 
        number=iterations
    ) for _ in range(iterations))

    time_iterate = sum(timeit.timeit(
        stmt=f"reverse_iterative('{test_data}')", 
        setup="", 
        number=iterations
    ) for _ in range(iterations)) / iterations # Average per call
    
    return f"Slicing: {time_slice_total:.4f}s (total), Avg={time_slice_total/iteractions:.6f}"

if __name__ == '__main__':
    # Hard-coded sample values as required, no user input or network access.
    print(f"\n{'='*50}")
    
    test_string = "a" * 1_000_000 # Reduced slightly for reliable execution in standard environments
    
    start = timeit.default_timer()
    rev_iterate_result = reverse_iterative(test_string)
    end = timeit.default_timer()

    print(f"\nTest String Length: {len(test_string)}")
    
    slice_str = test_string[::-1]
    iter_str = reverse_iterate_result
    
    # Comparison Logic within the module
    if len(slice_str) == 0 or len(iter_str) == 0: 
        is_faster_slice, reason = "No", "Error"
        result_type = f"Slicing (Length={len(slice_str)}) vs Iterative (Length={len(rev_iterate_result)}): {reason}"