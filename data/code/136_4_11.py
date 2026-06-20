def combine_flags(flag_a, flag_b, flag_c):
    return (flag_a << 2) | (flag_b << 1) | flag_c

if __name__ == '__main__':
    result = combine_flags(True, False, True)
    print(result)