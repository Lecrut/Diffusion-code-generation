import timeit

def reverse_iterative(s: str) -> str:
    """Reverse a string iteratively using a loop."""
    result = []
    for char in s[::-1]:  # Using slicing here to avoid O(n^2) append overhead, but logic is iterative
        result.append(char)
    return ''.join(result)

def reverse_iterative_simple(s: str) -> str:
    """Reverse a string iteratively using a simple loop without list comprehension tricks."""
    chars = []
    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i])
    return ''.join(chars)

def reverse_slicing(s: str) -> str:
    """Reverse a string using Python's slicing method."""
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for very long strings (e.g., 10 million characters)
    large_string = 'a' * 10_000_000
    
    # Benchmark the iterative method
    time_iterative = timeit.timeit(
        stmt=reverse_iterative_simple(large_string),
        setup='',
        number=3
    )
    
    # Benchmark the slicing method
    time_slicing = timeit.timeit(
        stmt=reverse_slicing(large_string),
        setup='',
        number=3
    )
    
    print(f"Time taken for iterative loop: {time_iterative:.4f} seconds")
    print(f"Time taken for slicing method:   {time_slicing:.4f} seconds")
    
    if time_slicing < time_iterative:
        result = reverse_slicing(large_string)
        print("Faster method used: Slicing")
    else:
        result = reverse_iterative_simple(large_string)
        print("Faster method used: Iterative Loop")