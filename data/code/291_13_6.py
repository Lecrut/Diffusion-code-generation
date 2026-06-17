def compare_lengths(a, b):
    if not isinstance(a, (str, list)) or not isinstance(b, (str, list)):
        raise TypeError("Both inputs must be strings or lists.")
    try:
        len_a = len(a)
        len_b = len(b)
    except TypeError:
        raise ValueError("One or both inputs could not be measured for length.")
    if len_a == len_b:
        return f"Lengths are equal. Length of A: {len_a}, Length of B: {len_b}"
    elif len_a > len_b:
        return f"Length of A is greater than Length of B. Length of A: {len_a}, Length of B: {len_b}"
    else:
        return f"Length of A is less than Length of B. Length of A: {len_a}, Length of B: {len_b}"
if __name__ == '__main__':
    print(compare_lengths("hello", "world"))
    print(compare_lengths(["a", "b"], ["c", "d", "e"]))
    print(compare_lengths([1, 2, 3], "abc"))
    print(compare_lengths("", ""))
    try:
        compare_lengths(123, "abc")
    except (TypeError, ValueError) as e:
        print(f"Error caught: {e}")
    try:
        compare_lengths(["a"], 100)
    except (TypeError, ValueError) as e:
        print(f"Error caught: {e}")