def is_single_bit_set(bitmask):
    return bitmask != 0 and (bitmask & (bitmask - 1)) == 0

if __name__ == '__main__':
    flags = [True, False, True]
    bitmask = sum(1 << i for i, flag in enumerate(flags) if flag)
    print(f"Bitmask: {bitmask}")
    print(f"Is mutually exclusive? {is_single_bit_set(bitmask)}")