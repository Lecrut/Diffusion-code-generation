def twos_complement_binary(n, bits=None):
    if bits is None:
        if n >= 0:
            bits = max(1, n.bit_length() + 1)
        else:
            bits = max(1, n.bit_length() + 2)
    if n < 0:
        mask = (1 << bits) - 1
        positive_repr = n & mask
        return bin(positive_repr)[2:].zfill(bits)
    else:
        return bin(n)[2:].zfill(bits)

if __name__ == '__main__':
    sample_values = [-1, -5, -10, 0, 5, 10, -128, 127]
    for value in sample_values:
        result = twos_complement_binary(value)
        print(result)