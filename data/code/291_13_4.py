def compare_lengths(a, b):
    if not isinstance(a, (str, list)) or not isinstance(b, (str, list)):
        raise TypeError("Both inputs must be strings or lists.")
    try:
        len_a = len(a)
        len_b = len(b)
    except TypeError as e:
        raise TypeError(f"Error calculating length for one of the inputs: {e}")
    if len_a == len_b:
        return f"Lengths are equal. Length: {len_a}"
    elif len_a > len_b:
        return f"Length of first input is greater. Length A: {len_a}, Length B: {len_b}"
    else:
        return f"Length of second input is greater. Length A: {len_a}, Length B: {len_b}"
if __name__ == '__main__':
    print(compare_lengths("hello", "world"))
    print(compare_lengths(["a", "b"], ["c", "d", "e"]))
    print(compare_lengths([1, 2, 3], "abc"))
    print(compare_lengths("", ""))
    try:
        compare_lengths(123, "test")
    except TypeError as e:
        print(f"Caught exception: {e}")
    try:
        compare_lengths([], {"a": "b"})
    except TypeError as e:
        print(f"Caught exception: {e}")