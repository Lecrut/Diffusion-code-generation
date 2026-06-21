def extract_third_value(tup):
    if not isinstance(tup, tuple):
        raise TypeError("Input must be a tuple")
    if len(tup) < 3:
        raise IndexError("Tuple must have at least three elements")
    return tup[2]

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    try:
        result = extract_third_value(sample_tuple)
        print(result)
    except (TypeError, IndexError) as e:
        print(e)

    empty_tuple = ()
    try:
        extract_third_value(empty_tuple)
    except IndexError:
        print("Handled empty tuple error")

    short_tuple = (1, 2)
    try:
        extract_third_value(short_tuple)
    except IndexError:
        print("Handled short tuple error")