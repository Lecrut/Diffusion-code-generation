def get_middle_element(t):
    if not t:
        raise ValueError("Tuple must not be empty")
    length = len(t)
    middle_index = (length - 1) // 2
    return t[middle_index]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = get_middle_element(sample_tuple)
    print(result)
    empty_tuple = ()
    try:
        get_middle_element(empty_tuple)
    except ValueError as e:
        print(f"ValueError: {e}")