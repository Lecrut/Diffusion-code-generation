import timeit

def reverse_iterative(s: str) -> str:
    """Reverses a string iteratively using a loop."""
    result = []
    for char in s:
        result.insert(0, char)  # Insert at beginning to build reversed string
    return ''.join(result)

def benchmark_and_return():
    """Benchmarks iterative and slicing methods on very long strings.
    
    Returns the faster method's implementation as a callable function."""
    sample_string = "A" * (10**7)  # Very long string: 10 million characters

    times_iterative = timeit.timeit(
        stmt="reverse_iterative(sample_string)",
        setup="from __main__ import reverse_iterative; sample_string",
        number=3,
    ) / 3

    times_slicing = timeit.timeit(
        stmt='"".join(reversed(sample_string))',
        setup=f"sample_string='{sample_string}'",
        number=3,
    ) / 3

    if times_iterative < times_slicing:
        return reverse_iterative
    else:
        def slice_reverse(s):
            return "".join(reversed(s))
        return slice_reverse

if __name__ == '__main__':
    best_method = benchmark_and_return()
    
    # Run the selected method on a fresh large string to demonstrate result
    test_string = "Hello, World! This is a very long string used for testing performance." * 100
    
    reversed_result = best_method(test_string)
    
    print("Reversed String:")
    print(reversed_result[:50] + "...")