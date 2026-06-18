import time

def reverse_string_recursive(s: str) -> str:
    """Recursively reverses a string."""
    if len(s) <= 1:
        return s
    else:
        return (reverse_string_recursive(s[1:]) + s[0])

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required
    test_strings = [
        "hello",
        "",
        "a" * 5,
        "Python Programming!",
    ]

    print("Recursive reversal results:")
    for t in test_strings:
        rev_t = reverse_string_recursive(t)
        print(f"{t!r} -> {rev_t!r}")

    # Time complexity analysis logic embedded here
    time_complexity_analysis = """
The recursive solution has a time complexity of O(n), where n is the length of the string.
This occurs because each function call processes one character and reduces the problem size by 1, leading to exactly n calls in total (excluding base case overhead).

Comparing it to direct slicing:
- Recursive approach: O(n) operations with significant stack overhead due to recursion depth. Memory usage is also O(n) for the call stack plus string construction during return values. In a standard system implementation using CPython, slices might be optimized but still create new objects, resulting in O(1) extra space per step until concatenation creates an O(k^2) worst-case scenario if repeated inefficiently (though Python optimizes this to O(n)).
- Slicing approach (`s[::-1]`): Typically O(n) for the reversal logic plus efficient memory allocation. The slicing operation is implemented in C, making it faster and more cache-friendly than the interpreted recursion overhead.

However, both have linear time complexity regarding input size: n calls/operations."""