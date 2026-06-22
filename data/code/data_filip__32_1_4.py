def binary_to_hex(num):
    hex_chars = '0123456789ABCDEF'
    if num == 0:
        return hex_chars[0]
    result = ''
    mask = 0xF
    while num > 0:
        digit = num & mask
        result = hex_chars[digit] + result
        num = num >> 4
    return result

def transform_list(binary_list):
    return [binary_to_hex(n) for n in binary_list]

if __name__ == '__main__':
    sample_values = [0, 1, 15, 16, 255, 4095, 65535]
    hex_values = transform_list(sample_values)
    print(hex_values)