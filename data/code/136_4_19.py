def combine_flags(flag_a: bool, flag_b: bool) -> bool:
    return flag_a & flag_b

if __name__ == '__main__':
    result = combine_flags(True, False)
    print(result)