def extract_third_value(t):
    if len(t) < 3:
        raise IndexError("Tuple must have at least three elements")
    return t[2]

if __name__ == '__main__':
    sample_tuples = [
        (1, 2, 3),
        ('a', 'b', 'c', 'd'),
        (True, False, None),
    ]
    for t in sample_tuples:
        print(extract_third_value(t))
    try:
        extract_third_value(())
    except IndexError as e:
        print(e)
    try:
        extract_third_value((1, 2))
    except IndexError as e:
        print(e)