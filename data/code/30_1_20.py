def get_twos_complement(n, bits=8):
    if n >= 0:
        return format(n, f'0{bits}b')
    if n < -(2 ** (bits - 1)) or n >= 2 ** (bits - 1):
        raise ValueError(f"Value {n} out of range for {bits}-bit signed integer")
    masked = n & ((1 << bits) - 1)
    return format(masked, f'0{bits}b')

if __name__ == '__main__':
    sample_values = [-1, -4, -8, -128]
    for val in sample_values:
        print(get_twos_complement(val))