def extract_third_value(t):
    if len(t) < 3:
        raise IndexError("Tuple must contain at least three elements.")
    return t[2]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40)
    result = extract_third_value(sample_tuple)
    print(result)
    try:
        empty_tuple = ()
        extract_third_value(empty_tuple)
    except IndexError as e:
        print(e)