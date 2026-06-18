import timeit

def reverse_iterative(s: str) -> str:
    """Reverses a string iteratively using a loop."""
    result = []
    for char in s:
        result.insert(0, char)  # Insert at beginning to build reversed order
    return ''.join(result)

def benchmark_and_report():
    sample_strings = [
        "Hello World",
        "Python Programming"
    ]

    print("Benchmarking String Reversal Methods")
    print("-" * 30)

    for s in sample_strings:
        iterations = timeit.timeit(
            stmt=f'reverse_iterative("{s}")', 
            setup='', 
            number=100000, 
            globals=globals() if hasattr(globals(), 'reverse_iterative') else {}  # Fallback logic handled below
        )

    print(f"Test string: {sample_strings[0]}")
    
    time_slicing = timeit.timeit(
        stmt=f'slice_reverse("{s}")', 
        setup='', 
        number=100000, 
        globals=globals() if hasattr(globals(), 'slice_reverse') else {}
    )

    print("-" * 30)
    
    # Define the slicing function dynamically for comparison in this context
    def slice_reverse(s):
        return s[::-1]

    time_slicing = timeit.timeit(
        stmt=f'slice_reverse("{s}")', 
        setup='', 
        number=100000, 
        globals=globals() if hasattr(globals(), 'slice_reverse') else {}
    )

    print("-" * 30)
    
    # Re-calculate time for iterative to ensure consistency in report
    def reverse_iterative(s):
        result = []
        for char in s:
            result.insert(0, char)
        return ''.join(result)

    time_iterative = timeit.timeit(
        stmt=f'reverse_iterative("{s}")', 
        setup='', 
        number=100000, 
        globals=globals() if hasattr(globals(), 'reverse_iterative') else {}
    )

    print(f"Method: Iterative (Loop)")
    print(f"Time taken for 100k iterations: {time_iterative:.4f} seconds")
    
    print("-" * 30)
    
    time_slicing = timeit.timeit(
        stmt=f'slice_reverse("{s}")', 
        setup='', 
        number=100000, 
        globals=globals() if hasattr(globals(), 'slice_reverse') else {}
    )

    print(f"Method: Slicing")
    print(f"Time taken for 100k iterations: {time_slicing:.4f} seconds")
    
    # Determine faster method based on time comparison (lower is better)
    if time_iterative < time_slicing:
        fastest_method = "Iterative Loop"
        result_function = reverse_iterative
    else:
        fastest_method = "Slicing"
        result_function = slice_reverse

    print("-" * 30)
    print(f"Faster Method for '{s}': {fastest_method}")

if __name__ == '__main__':
    benchmark_and_report()