def get_third_value(t):
    if not t:
        raise ValueError("Tuple is empty")
    if len(t) < 3:
        raise IndexError("Tuple does not contain a third value")
    return t[2]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40)
    result = get_third_value(sample_tuple)
    print(result)
    try:
        get_third_value(())
    except ValueError as e:
        print(e)
    try:
        get_third_value((1, 2))
    except IndexError as e:
        print(e)