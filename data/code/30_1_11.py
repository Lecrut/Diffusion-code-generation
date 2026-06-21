def to_twos_complement(n, bits=None):
    if n >= 0:
        if bits is None:
            return bin(n)[2:]
        else:
            return bin(n)[2:].zfill(bits)
    else:
        if bits is None:
            bits = n.bit_length() + 1
        mask = (1 << bits) - 1
        twos_complement = n & mask
        return bin(twos_complement)[2:].zfill(bits)

def to_signed_integer(binary_str):
    bits = len(binary_str)
    value = int(binary_str, 2)
    if binary_str[0] == '1':
        value -= 1 << bits
    return value
if __name__ == '__main__':
    test_values = [0, 1, -1, 5, -5, 255, -255, 127, -128]
    for val in test_values:
        binary_repr = to_twos_complement(val)
        recovered_val = to_signed_integer(binary_repr)
        print(f'{val} -> {binary_repr} -> {recovered_val}')