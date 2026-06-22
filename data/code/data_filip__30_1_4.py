def to_twos_complement(n, bits=8):
    if n >= 0:
        binary = bin(n)[2:]
        if len(binary) > bits:
            raise ValueError(f"Value {n} does not fit in {bits} bits")
        return binary.zfill(bits)
    else:
        if n < -(2**(bits - 1)):
            raise ValueError(f"Value {n} is out of range for {bits} bits")
        mask = 2**bits
        result = bin(mask + n)[2:]
        if len(result) > bits:
            raise ValueError(f"Value {n} does not fit in {bits} bits")
        return result.zfill(bits)

if __name__ == '__main__':
    positive_value = 5
    negative_value = -5
    zero_value = 0
    min_val = -128
    max_val = 127

    print(to_twos_complement(positive_value, 8))
    print(to_twos_complement(negative_value, 8))
    print(to_twos_complement(zero_value, 8))
    print(to_twos_complement(min_val, 8))
    print(to_twos_complement(max_val, 8))