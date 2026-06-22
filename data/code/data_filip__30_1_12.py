def int_to_twos_complement(n, bits=32):
    if n < -(2 ** (bits - 1)) or n >= 2 ** (bits - 1):
        raise ValueError(f"Value {n} out of range for {bits} bits")
    if n >= 0:
        return bin(n)[2:].zfill(bits)
    else:
        return bin((1 << bits) + n)[2:]

def main():
    result_positive = int_to_twos_complement(5)
    print(result_positive)
    result_negative = int_to_twos_complement(-5)
    print(result_negative)
    result_zero = int_to_twos_complement(0)
    print(result_zero)

if __name__ == '__main__':
    main()