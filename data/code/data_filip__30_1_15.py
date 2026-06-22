def to_twos_complement(value, bits=None):
    if bits is None:
        if value >= 0:
            return bin(value)[2:]
        bit_length = value.bit_length()
        bits = bit_length + 2
    if value < 0:
        value = (1 << bits) + value
    return bin(value)[2:].zfill(bits)

if __name__ == '__main__':
    test_values = [-1, -5, -100, 0, 42]
    for num in test_values:
        result = to_twos_complement(num, 8)
        print(f"{num}: {result}")
    for num in test_values:
        result = to_twos_complement(num)
        print(f"{num} (auto bits): {result}")