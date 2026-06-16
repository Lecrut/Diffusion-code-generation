def compare_lengths(input1, input2):
    if not isinstance(input1, (str, list)) or not isinstance(input2, (str, list)):
        raise TypeError("Both inputs must be strings or lists.")
    try:
        len1 = len(input1)
        len2 = len(input2)
    except TypeError as e:
        raise TypeError(f"Error calculating length: {e}")
    result = "Equal" if len1 == len2 else f"Input 1 length ({len1}) is not equal to Input 2 length ({len2})"
    return result
if __name__ == '__main__':
    print(compare_lengths("hello", "world"))
    print(compare_lengths(["a", "b"], ["c", "d"]))
    print(compare_lengths("abc", ["a", "b", "c"]))
    try:
        compare_lengths(123, "test")
    except TypeError as e:
        print(f"Caught exception: {e}")
    try:
        compare_lengths("abc", 12345)
    except TypeError as e:
        print(f"Caught exception: {e}")