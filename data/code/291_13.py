def compare_lengths(input1, input2):
    if not isinstance(input1, (str, list)):
        raise TypeError("First input must be a string or a list.")
    if not isinstance(input2, (str, list)):
        raise TypeError("Second input must be a string or a list.")
    try:
        len1 = len(input1)
    except TypeError:
        raise ValueError("Input 1 is invalid for length calculation.")
    try:
        len2 = len(input2)
    except TypeError:
        raise ValueError("Input 2 is invalid for length calculation.")
    if len1 == len2:
        return f"Lengths are equal: {len1}"
    elif len1 > len2:
        return f"Length of input1 ({len1}) is greater than length of input2 ({len2})"
    else:
        return f"Length of input1 ({len1}) is less than length of input2 ({len2})"
if __name__ == '__main__':
    print(compare_lengths("hello", "world"))
    print(compare_lengths(["a", "b"], ["c", "d", "e"]))
    print(compare_lengths([1, 2, 3], [4, 5]))
    print(compare_lengths("", ""))
    print(compare_lengths("abc", "ab"))
    try:
        compare_lengths(123, "test")
    except (TypeError, ValueError) as e:
        print(f"Error caught: {e}")
    try:
        compare_lengths(["a"], 100)
    except (TypeError, ValueError) as e:
        print(f"Error caught: {e}")