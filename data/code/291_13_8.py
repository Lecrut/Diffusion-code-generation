def compare_lengths(a, b):
    try:
        len_a = len(a)
    except TypeError:
        raise TypeError("First argument must be a sequence type (string or list).")
    try:
        len_b = len(b)
    except TypeError:
        raise TypeError("Second argument must be a sequence type (string or list).")
    if not isinstance(a, (str, list)) or not isinstance(b, (str, list)):
        raise TypeError("Both inputs must be strings or lists.")
    result = len_a - len_b
    return f"Length of first input ({a}): {len_a}, Length of second input ({b}): {len_b}, Difference: {result}"
if __name__ == '__main__':
    print(compare_lengths("hello", "world"))
    print(compare_lengths([1, 2, 3], ["a", "b"]))
    try:
        compare_lengths("test", 123)
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        compare_lengths(10, "abc")
    except TypeError as e:
        print(f"Error caught: {e}")