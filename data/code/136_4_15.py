def combine_flags(flag_a: bool, flag_b: bool, flag_c: bool) -> bool:
    return (flag_a & flag_b) | ~flag_c

if __name__ == '__main__':
    result = combine_flags(True, False, True)
    print(result)