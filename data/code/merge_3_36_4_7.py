import timeit

def reverse_iterative(s: str) -> str:
    """Reverse a string using an iterative loop."""
    result = []
    for char in reversed(s):
        result.append(char)
    return ''.join(result)

def benchmark_and_return():
    # Hard-coded sample values to avoid any input requirements or file access.
    long_string = "x" * 10_000_000

    times_iterative = timeit.timeit(
        stmt=f'reverse_iterative("{long_string}")',
        setup='',
        number=5,
    ) / 5

    times_slicing = timeit.timeit(
        stmt='f"{long_string[::-1]}"',
        setup='',
        number=5,
    ) / 5

    if times_iterative < times_slicing:
        return "Iterative method is faster."
    else:
        return "Slicing method is faster or equal."

if __name__ == '__main__':
    result = benchmark_and_return()
    print(result)