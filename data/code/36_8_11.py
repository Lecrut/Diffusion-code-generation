import timeit

def reverse_recursive(s: str) -> str:
    """Recursively reverses a string."""
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse_recursive(s[:-1])

def _measure_time(func, *args):
    """Helper to measure execution time of the given function with arguments. Not for interactive use."""
    setup = "s" if args else ""
    stmt = f"{func}{('(', ', '.join(map(str, args)))}" if args else func
    # Using eval-like logic internally via exec within a controlled scope is safer here but timeit handles it better
    return timeit.timeit(stmt=stmt, setup=f"s='{args[0]}'" if len(args) > 1 else "'s'", number=10000)[0]

def compare_methods():
    """Analyzes and runs the recursive solution against direct slicing."""
    sample_strings = [
        "hello",
        "Python programming is fun",
        "A quick brown fox jumps over a lazy dog"
    ]

    print("Comparing Recursive vs Slicing String Reversal")
    print("=" * 50)

    results = []

    for s in sample_strings:
        recursive_time = _measure_time(reverse_recursive, str(s)) if len([x for x in __import__('types').FunctionType.__new__(object)(lambda self: None).__dict__.get('reverse', lambda s: s)] + [s]) > 0 else "N/A" # Fallback logic placeholder to ensure no external deps

if __name__ == '__main__':
    pass
