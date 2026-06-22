def binary_to_hex(bit_list):
    if not bit_list:
        return "0"
    num = 0
    for bit in bit_list:
        num = (num << 1) | bit
    if num == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    if num < 0:
        num = num + (1 << 64)
    result = ""
    while num > 0:
        remainder = num & 15
        result = hex_chars[remainder] + result
        num = num >> 4
    return result

if __name__ == '__main__':
    sample_bits = [1, 0, 1, 1, 0, 1]
    print(binary_to_hex(sample_bits))
    print(binary_to_hex([1, 1, 1, 1, 1, 1, 1, 1]))
    print(binary_to_hex([0, 0, 0, 0, 1, 0, 1, 1]))