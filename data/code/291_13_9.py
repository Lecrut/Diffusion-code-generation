def compare_lengths(input1, input2):
    if not isinstance(input1, (str, list)) or not isinstance(input2, (str, list)):
        raise TypeError("Both inputs must be strings or lists.")
    try:
        len1 = len(input1)
        len2 = len(input2)
    except TypeError as e:
        raise TypeError(f"Error calculating length: {e}")
    result = "Equal" if len1 == len2 else f"Different (Len1: {len1}, Len2: {len2})"
    return result
if __name__ == '__main__':
    print(compare_lengths("hello", "world"))
    print(compare_lengths(["a", "b"], ["c", "d", "e"]))
    print(compare_lengths([1, 2, 3], [4, 5]))
    try:
        compare_lengths("test", 123)
    except TypeError as e:
        print(f"Caught Exception: {e}")
    try:
        compare_lengths(None, "test")
    except TypeError as e:
        print(f"Caught Exception: {e}")