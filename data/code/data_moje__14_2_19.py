def get_third_value(t):
    if len(t) < 3:
        raise ValueError("Tuple must contain at least three elements")
    return t[2]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40)
    print(get_third_value(sample_tuple))
    empty_tuple = ()
    try:
        get_third_value(empty_tuple)
    except ValueError as e:
        print(e)