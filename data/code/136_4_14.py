def combine_flags(flag_a, flag_b):
    return (flag_a << 1) | flag_b

if __name__ == '__main__':
    result = combine_flags(True, False)
    print(result)