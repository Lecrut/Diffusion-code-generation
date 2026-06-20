def bitwise_operations(flag1, flag2):
    and_result = flag1 & flag2
    or_result = flag1 | flag2
    not_result = ~flag1
    return and_result, or_result, not_result

if __name__ == '__main__':
    sample_flags = (0b1010, 0b1100)
    results = bitwise_operations(*sample_flags)
    print(results)