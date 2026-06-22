def binary_to_hex(binary_string):
    num = int(binary_string, 2)
    hex_str = hex(num)[2:]
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str
    return hex_str.upper()

if __name__ == '__main__':
    sample_binary = "11010110110100101000111110011010"
    result = binary_to_hex(sample_binary)
    print(result)