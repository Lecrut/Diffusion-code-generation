def is_bit_set_once(bitmask):
    return bitmask & (bitmask - 1) == 0

if __name__ == '__main__':
    flags = [True, False, True]
    bitmask = sum(1 << i for i, flag in enumerate(flags) if flag)
    print(f"Bitmask: {bin(bitmask)}")
    print(f"Mutually exclusive? {is_bit_set_once(bitmask)}")