import sys

def int_to_twos_complement(n, bits=8):
    if n < 0:
        mask = (1 << bits) - 1
        return format(n & mask, f'0{bits}b')
    return format(n, f'0{bits}b')

def twos_complement_to_int(binary_str, bits=None):
    if bits is None:
        bits = len(binary_str)
    if binary_str[0] == '1':
        value = int(binary_str, 2) - (1 << bits)
        return value
    return int(binary_str, 2)

if __name__ == '__main__':
    test_values = [-5, -128, 0, 7, -1]
    for val in test_values:
        binary_rep = int_to_twos_complement(val, 8)
        recovered_val = twos_complement_to_int(binary_rep, 8)
        print(f'{val}: {binary_rep} -> {recovered_val}')