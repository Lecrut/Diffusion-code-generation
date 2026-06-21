def binary_to_hex(binary_string):
    if not binary_string:
        return ''
    decimal_value = int(binary_string, 2)
    hex_string = hex(decimal_value)[2:]
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string
    return hex_string.upper()

if __name__ == '__main__':
    sample_binary = '11010110'
    result = binary_to_hex(sample_binary)
    print(result)