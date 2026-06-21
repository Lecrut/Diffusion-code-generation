def to_twos_complement(n: int, bits: int) -> str:
    if n < 0:
        return format((1 << bits) + n, f'0{bits}b')
    return format(n, f'0{bits}b')

if __name__ == '__main__':
    sample_values = [-5, -1, 0, 10, -128]
    for value in sample_values:
        if value < 0:
            bits = max(8, (value.bit_length() + 1) if value != -1 else 1)
        else:
            bits = max(8, value.bit_length() + 1 if value != 0 else 1)
        result = to_twos_complement(value, bits)
        print(f"{value} in {bits}-bit two's complement: {result}")