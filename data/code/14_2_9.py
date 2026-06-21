def get_third_value(t):
    if not t:
        raise ValueError("Tuple must contain at least three elements")
    if len(t) < 3:
        raise ValueError("Tuple must contain at least three elements")
    return t[2]

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40)
    result = get_third_value(sample_tuple)
    print(result)