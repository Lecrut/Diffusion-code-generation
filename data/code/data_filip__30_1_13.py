def to_twos_complement_binary(n):
    if n >= 0:
        if n == 0:
            return '0'
        return bin(n)[2:]
    else:
        bit_length = n.bit_length() + 1
        mask = (1 << bit_length) - 1
        twos_comp = ~n + 1 & mask
        return bin(twos_comp)[2:].zfill(bit_length)
if __name__ == '__main__':
    test_values = [0, 1, -1, 2, -2, 5, -5, 127, -127, 255, -255]
    for val in test_values:
        print(to_twos_complement_binary(val))