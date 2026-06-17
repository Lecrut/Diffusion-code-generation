def compare_lengths(a, b):
    try:
        len_a = len(a)
    except TypeError:
        raise TypeError("First argument must be a sequence (string or list).")
    try:
        len_b = len(b)
    except TypeError:
        raise TypeError("Second argument must be a sequence (string or list).")
    if not isinstance(a, (str, list)) or not isinstance(b, (str, list)):
        raise TypeError("Both inputs must be strings or lists.")
    result = "Equal" if len_a == len_b else f"Different: {len_a} vs {len_b}"
    return result
if __name__ == '__main__':
    print(compare_lengths("hello", "world"))
    print(compare_lengths([1, 2, 3], ['a', 'b']))
    print(compare_lengths("abc", "abcd"))
    print(compare_lengths([], []))
    try:
        compare_lengths(123, "test")
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        compare_lengths("a", 10)
    except TypeError as e:
        print(f"Error caught: {e}")