import math

def integer_to_twos_complement(n: int) -> str:
    if n == 0:
        return '0'
    if n > 0:
        return bin(n)[2:]
    abs_n = -n
    bit_length = abs_n.bit_length()
    width = bit_length + 1
    mask = (1 << width) - 1
    twos_complement_value = n & mask
    binary_str = bin(twos_complement_value)[2:]
    return binary_str.zfill(width)

def main():
    values = [0, 1, -1, 10, -10, 127, -128, 128, -129]
    for val in values:
        result = integer_to_twos_complement(val)
        print(f'{val:>5} -> {result}')
if __name__ == '__main__':
    main()