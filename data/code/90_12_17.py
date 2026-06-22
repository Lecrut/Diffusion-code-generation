def check_or_condition(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Arguments must be boolean types")
    int_a = a & 1
    int_b = b & 1
    return bool(int_a | int_b)

if __name__ == '__main__':
    a_val = True
    b_val = False
    output = check_or_condition(a_val, b_val)
    print(output)