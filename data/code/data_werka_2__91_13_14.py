def negate_boolean(value: bool) -> bool:
    bit_mask = {True: 0, False: 1}
    inverted_bit = bit_mask[value] ^ 1
    result_map = {0: False, 1: True}
    return result_map[inverted_bit]

if __name__ == '__main__':
    print(negate_boolean(True))
    print(negate_boolean(False))