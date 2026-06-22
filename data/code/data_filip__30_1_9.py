def to_twos_complement(n, bits=8):
    if n >= 0:
        return format(n, f'0{bits}b')
    return format((1 << bits) + n, f'0{bits}b')

if __name__ == '__main__':
    sample_values = [-5, -1, -128, 0, 7, -100]
    bit_width = 8
    for value in sample_values:
        result = to_twos_complement(value, bit_width)
        print(f'{value:4d} -> {result}')